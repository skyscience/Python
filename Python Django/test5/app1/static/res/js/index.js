var curWallet = "";
function getWallectInfo() {
    window.postMessage({
        "target": "contentscript",
        "data": {},
        "method": "getAccount",
    }, "*");
    window.addEventListener('message', function (e) {
        if (e.data && e.data.data) {
            if (e.data.data.account) {
            	curWallet = e.data.data.account;
            	getSharesFromNasChain(curWallet);
            }
        }
    });
}


var shares = [];
var recentlyShares = [];
var fireShares = [];
var searchShares = [];
function getSharesFromNasChain(curWallet){
	query(curWallet,config.getShareList,'',function(data){
		if(data.execute_err==""){
			shares = JSON.parse(data.result);
			recentlyShares = shares.reverse();
			fireShares = _.sortBy(shares, [function(o) { return o.comments.length + o.profits.length; }]);
			fireShares = fireShares.reverse();
			displayNewShareContent(recentlyShares);
			displayFireShareContent(fireShares);
		}
	});
}
function pullRecentlyShares(obj){
	if(!displayNewShareContent(recentlyShares)){
		$(obj).html('No more');
	}
}
function pullFireShares(obj){
	if(!displayFireShareContent(fireShares)){
		$(obj).html('No more');
	}
}
function pullSearchShares(obj){
	if(!displaySearchResult(searchShares)){
		$(obj).html('No more');
	}
}

function publicShare(){
	var modal = $('#modal1')
	modal.find('.modal-title').text('发起拍卖');
	var html = [];
	html.push('<div class="alert alert-warning px-3 text-center small">');
	// html.push('<i class="fas fa-exclamation-triangle"></i> NULL ');
	html.push('</div>');
	html.push('<form class="share-form" novalidate><div class="form-group">');
	html.push('<label for="exampleInputEmail1">物品名称</label>');
	html.push('<input type="text" class="form-control" id="shareTitle" aria-describedby="shareTitleHelp" required>');
	html.push('<div class="invalid-feedback"> 请输入名称. </div>');
	html.push('</div>');
	html.push('<div class="form-group">');
	html.push('<label for="shareContentlabel">物品介绍</label>');
	html.push('<textarea class="form-control" rows=5 id="shareContent" required></textarea>');
	html.push('<div class="invalid-feedback"> 请输入内容. </div>');
	html.push('</div></form>');
	html.push('<div class="row justify-content-md-center pt-2">');
	html.push('<div class="col col-sm-2 px-3 text-center">');
	html.push('<button type="button" class="btn btn-dark" onclick=sendShare();>发起拍卖</button>');
	html.push('</div></div>');
	modal.find('.modal-body').html('');
	modal.find('.modal-body').html(html.join(''));
	modal.modal('show');
}
function sendShare(){
	var forms = document.getElementsByClassName('share-form');
	var validation = Array.prototype.filter.call(forms, function(form) {
		if (form.checkValidity() === false) {
			event.preventDefault();
			event.stopPropagation();
		}else{
			var title = $('#shareTitle').val();
			var shareContent = $('#shareContent').val();
			var args = [{title:title,shareBody:shareContent}];
			defaultOptions.listener = function(data){
				if(typeof data === "object"){
					tips('发起拍卖成功，大约15秒后数据打包写入区块链，请稍后刷新查看。',true);
				}else{
					tips(data,false);
				}
			};
			nebPay.call(config.contractAddr,"0",config.share,JSON.stringify(args),defaultOptions);
		}
		form.classList.add('was-validated');
	});
}



function bindSearchBtn(){
	$('.search-btn').click(function(){
		var keyword = $('#keyword').val();
		if(keyword == ""){
			$('#keyword').focus();
			tips('请输入关键字');
		}else{
			search(keyword);
		}
	});
}
function search(keyword){
	$('.indexDefault').hide();
	$('.searchContainer').show();
	var reg = new RegExp(keyword);
	searchShares = _.filter(recentlyShares, function(o) {
		if(o.title.match(reg) || o.shareBody.match(reg)){
			return true;
		}else{
			return false;
		}
	});
	$('.searchShareContainer').html('');
	console.log(searchShares);
	displaySearchResult(searchShares);
}
function displaySearchResult(data){
	return initShareDisplay(data,'searchShareContainer');
}
function displayNewShareContent(data){
	return initShareDisplay(data,'newShareContainer');
}

function displayFireShareContent(data){
	return initShareDisplay(data,'fireShareContainer');
}
var pageSize = 5;
function initShareDisplay(data,containerClass){
	$('.'+containerClass).find('.lodingdiv').remove();
	var displaySize = $('.'+containerClass).find('.media').length;
	var count = data.length;
	if(displaySize == count){return false}
	var loop = displaySize + pageSize;
	if(count  < (displaySize+pageSize)){
		loop = count;
	}
	var html = [];
	for(var i=displaySize;i<loop;i++){
		var color = randomColor();
		html.push('<div class="media text-muted pt-3">');
		html.push('<img data-src="holder.js/32x32?theme=thumb&amp;bg='+color+'&amp;fg='+color+'&amp;size=1" alt="32x32" class="mr-2 rounded" style="width: 32px; height: 32px;"  data-holder-rendered="true">');
		html.push('<p class="media-body pb-1 mb-0 small lh-125">');
		html.push('<strong class="d-block text-gray-dark sharetitle" data-toggle="modal" data-target="#modal1" data-sid='+data[i].id+'>'+data[i].title+'</strong>');
		html.push(data[i].shareBody);
		html.push('</p>');
		html.push('</div>');
		html.push('<div class="text-muted media-body pb-1 mb-0 small lh-125 border-bottom border-gray">');
		html.push('<span class="d-block mt-2 text-right">');
		html.push('<i class="far fa-calendar-alt"></i><span id="createtime">'+new Date(data[i].createtime*1000).toLocaleString()+'</span>');
		html.push('<span class="reply" data-toggle="modal" data-target="#modal1" data-sid='+data[i].id+' title="评价"><i class="far fa-comment-alt"></i>&nbsp;&nbsp;'+data[i].comments.length+'</span>');
		html.push('<span class="reward" data-toggle="modal" data-target="#modal1" data-sid='+data[i].id+' title="最高竞拍价"><i class="far fa-credit-card"></i>&nbsp;&nbsp;'+calcReward(data[i].profits)+'&nbsp;NAS</span>');
		html.push('</span></div>');
	}
	$('.'+containerClass).append(html.join(''));
	Holder.run();
	return true;
}

function initModal(target){
	if(target.hasClass('sharetitle')){
		showShareInfoInModal(target.data('sid'));
	}else  if(target.hasClass('reply')){
		quickReplyInModal(target.data('sid'));
	}else if(target.hasClass('reward')){
		quickRewardInModal(target.data('sid'));
	}
}
function showShareInfoInModal(sid){
	var share = getShareInfo(sid);
	comments = share.comments.reverse();
	var modal = $('#modal1')
	modal.find('.modal-title').text('查看共享内容');
	var html = [];
	html.push('<p class="text-lg-center">'+share.title+'</p>');
	html.push('<p class="text-center text-gray-dark small text-muted">作者：'+ share.ownner +" 发布时间："+ new Date(share.createtime*1000).toLocaleString()+'</p>');
	html.push('<span class="text-md-left text-muted">'+share.shareBody+'</span>');
	html.push('<div class="container">');
	html.push('<div class="row justify-content-md-center border-top pt-2">');
	html.push('<div class="col col-sm-2 px-3 text-center">');
	html.push('<button type="button" class="btn btn-dark replyBtn" sid='+sid+' style="width:80px;">回复</button><p class="text-secondary small mt-1">共有回复'+share.comments.length+'条</p>');
	html.push('</div>');
	html.push('<div class="col col-sm-2 px-3 text-center">');
	html.push('<button type="button" class="btn btn-danger rewardBtn" sid='+sid+' style="width:80px;">赏</button><p class="text-secondary small mt-1">共竞拍'+share.profits.length+'次</p>');
	html.push('</div>');
	html.push('</div></div>');
	//reply
	html.push('<div class="container shareReplys"></div>');
	modal.find('.modal-body').html('');
	modal.find('.modal-body').html(html.join(''));
	bindReplyRewardBtnClick();
	genShareReply(0);
}
var comments = [];
function genShareReply(page){
	var size = 3;	
	var len = comments.length;
	var loop = (size * page + size)>len ?  len : size * page + size;
	var html = [];
	for(var i=size * page;i<loop;i++){
		var color = randomColor();
		html.push('<div class="media text-muted pt-3">');
		html.push('<img data-src="holder.js/32x32?theme=thumb&amp;bg='+color+'&amp;fg='+color+'&amp;size=1" alt="32x32" class="mr-2 rounded" style="width: 32px; height: 32px;"  data-holder-rendered="true">');
		html.push('<p class="media-body pb-1 mb-0 small lh-125">');
		html.push('<strong class="d-block text-gray-dark">'+comments[i].name+'</strong>');
		html.push(comments[i].text);
		html.push('</p>');
		html.push('</div>');
		html.push('<div class="text-muted media-body pb-1 mb-0 small lh-125 border-bottom border-gray">');
		html.push('<span class="d-block text-right">');
		html.push('<i class="far fa-calendar-alt"></i><span id="createtime">'+new Date(comments[i].time*1000).toLocaleString()+'</span>');
		html.push('<i class="far fa-user-circle"></i><span>&nbsp;&nbsp;'+comments[i].wallet+'</span>');
		html.push('</span></div>');
	}
	html.push('<div class="row text-muted mt-2 justify-content-md-center">');
	if(page == 0 && len>(size * page + size)){
		html.push('<button type="button" class="btn btn-secondary m-1" onclick=genShareReply('+(page+1)+')>下一页</button>');
	}else if(page != 0 && (size * page + size)>=len){
		html.push('<button type="button" class="btn btn-secondary m-1" onclick=genShareReply('+(page-1)+')>上一页</button>');
	}else if(page != 0 && (size * page + size) < len){
		html.push('<button type="button" class="btn btn-secondary m-1" onclick=genShareReply('+(page-1)+')>上一页</button>');
		html.push('<button type="button" class="btn btn-secondary m-1" onclick=genShareReply('+(page+1)+')>下一页</button>');
	}
	html.push('</div>');
	$('.shareReplys').html('');
	$('.shareReplys').html(html.join(''));
	Holder.run();
}
function bindReplyRewardBtnClick(){
	$('.replyBtn').unbind('click').click(function(){
		quickReplyInModal($(this).attr('sid'));
	});
	$('.rewardBtn').unbind('click').click(function(){
		quickRewardInModal($(this).attr('sid'));
	});
}
function quickReplyInModal(sid){
	var share = getShareInfo(sid);
	var modal = $('#modal1')
	modal.find('.modal-title').text('快速回复');
	var html = [];
	html.push('<p class="text-lg-center">回复名称：'+share.title+'</p>');
	html.push('<form class="reply-form" novalidate><div class="form-group">');
	html.push('<label for="exampleInputEmail1">回复人</label>');
	html.push('<input type="text" class="form-control" id="replyName" aria-describedby="replyNameHelp" required>');
	html.push('<div class="invalid-feedback"> 请输入昵称. </div>');
	html.push('</div>');
	html.push('<div class="form-group">');
	html.push('<label for="replyContentlabel">回复内容</label>');
	html.push('<textarea class="form-control" id="replyContent" required></textarea>');
	html.push('<div class="invalid-feedback"> 请输入回复内容. </div>');
	html.push('</div></form>');
	html.push('<div class="row justify-content-md-center pt-2">');
	html.push('<div class="col col-sm-2 px-3 text-center">');
	html.push('<button type="button" class="btn btn-dark" onclick=sendReply("'+sid+'");>提交回复</button>');
	html.push('</div></div>');
	modal.find('.modal-body').html('');
	modal.find('.modal-body').html(html.join(''));
}
function sendReply(sid){
	var forms = document.getElementsByClassName('reply-form');
	var validation = Array.prototype.filter.call(forms, function(form) {
		if (form.checkValidity() === false) {
			event.preventDefault();
			event.stopPropagation();
		}else{
			var name = $('#replyName').val();
			var replyContent = $('#replyContent').val();
			var args = [sid,{name:name,text:replyContent}];
			defaultOptions.listener = function(data){
				if(typeof data === "object"){
					tips('发布回复成功，大约15秒后数据打包写入区块链，请稍后刷新查看。',true);
				}else{
					tips(data,false);
				}
			};
			nebPay.call(config.contractAddr,"0",config.reply,JSON.stringify(args),defaultOptions);
		}
		form.classList.add('was-validated');
	});
}
function quickRewardInModal(sid){
	var share = getShareInfo(sid);
	var modal = $('#modal1');
	modal.find('.modal-title').text('加价');
	var html = [];
	html.push('<p class="text-lg-center">加价物品名称：'+share.title+'</p>');
	html.push('<div class="row justify-content-md-center pt-2">');
	html.push('<button type="button" class="btn btn-outline-danger m-2 rewardValueBtn" nas=0.00001>0.00001<small>&nbsp;NAS</small></button>');
	html.push('<button type="button" class="btn btn-outline-danger m-2 rewardValueBtn" nas=0.0001>0.0001<small>&nbsp;NAS</small></button>');
	html.push('<button type="button" class="btn btn-outline-danger m-2 rewardValueBtn" nas=0.001>0.001<small>&nbsp;NAS</small></button>');
	html.push('<button type="button" class="btn btn-outline-danger m-2 rewardValueBtn" nas=0.01>0.01<small>&nbsp;NAS</small></button>');
	html.push('</div><div class="row justify-content-md-center pt-2">');
	html.push('<button type="button" class="btn btn-outline-danger m-2 rewardValueBtn" nas=0.1>0.1<small>&nbsp;NAS</small></button>');
	html.push('<button type="button" class="btn btn-outline-danger m-2 rewardValueBtn" nas=1>1<small>&nbsp;NAS</small></button>');
	html.push('<button type="button" class="btn btn-outline-danger m-2 rewardValueBtn" nas=10>10<small>&nbsp;NAS</small></button>');
	html.push('<button type="button" class="btn btn-outline-danger m-2 rewardValueBtn" nas=100>100<small>&nbsp;NAS</small></button>');
	html.push('<button type="button" class="btn btn-outline-danger m-2 rewardValueBtn" nas=1000>1000<small>&nbsp;NAS</small></button>');
	html.push('</div>');
	html.push('<div class="row justify-content-md-center pt-2">');
	html.push('<div class="col col-sm-2 px-3 text-center">');
	html.push('<button type="button" class="btn btn-danger" onclick="sendReward(\''+sid+'\');">确认加价</button>');
	html.push('</div></div>');
	modal.find('.modal-body').html('');
	modal.find('.modal-body').html(html.join(''));
	$('.rewardValueBtn').unbind('click').click(function(){
		$('.rewardValueSelectedBtn').removeClass('rewardValueSelectedBtn');
		$(this).addClass('rewardValueSelectedBtn');
	});
}
function sendReward(sid){
	if($('.rewardValueSelectedBtn').length == 0){
		alert('请您选择加价金额。');
	}else{
		var value = $('.rewardValueSelectedBtn').attr('nas');
		var args = [sid];
		defaultOptions.listener = function(data){
			if(typeof data === "object"){
				tips('加价成功，大约15秒后数据打包写入区块链，请稍后刷新查看。',true);
			}else{
				tips(data,false);
			}
		};
		nebPay.call(config.contractAddr,value,config.reward,JSON.stringify(args),defaultOptions);
	}
}
function getShareInfo(sid){
	return _.find(shares, function(o) { return o.id == sid; });
}
function bindReplyClick(){
	$('#addNewVote').unbind('click').click(function(){
		var forms = document.getElementsByClassName('needs-validation');
		var validation = Array.prototype.filter.call(forms, function(form) {
			if (form.checkValidity() === false) {
				event.preventDefault();
				event.stopPropagation();
			}else{
				var args = $('.needs-validation').serializeArray();
				var votetitle = "",starttime="",endtime="";
				var opts = [];
				$.each(args,function(index,item){
					if(item.name == "votetitle"){
						votetitle = item.value;
					}else if(item.name == "starttime"){
						starttime = item.value;
					}else if(item.name == "endtime"){
						endtime = item.value;
					}else{
						opts.push(item.name+'='+item.value);
					}
				});
				starttime = new Date(starttime).getTime();
				endtime = new Date(endtime).getTime();
				addVote(votetitle,starttime,endtime,opts.join('@'));
			}
			form.classList.add('was-validated');
		});
	});
}
$(function(){
	//getWallectInfo();
	getSharesFromNasChain("n1MptFSrpovW66uFyZyaqLdEtcc6eyBixZY");
	bindSearchBtn();
	$('#modal1').on('show.bs.modal', function (event) {
		  var target = $(event.relatedTarget);
		  var sid = target.data('sid') ;
		  initModal(target);
	});
});
