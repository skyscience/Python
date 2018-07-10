var curWallet = "";
function getWallectInfo() {
    window.postMessage({
        "target": "contentscript",
        "data": {},
        "method": "getAccount",
    }, "*");
    window.addEventListener('message', function (e) {
        if (e.data && e.data.data) {
            if (e.data.data.account) {//这就是当前钱包中的地址
            	curWallet = e.data.data.account;
            	getSharesFromNasChain(curWallet);
				queryPersonalData(curWallet);
            }
        }
    });
}

var shares = [];
function getSharesFromNasChain(addr){
	neb.setRequest(new nebulas.HttpRequest(config.apiPrefix));
	neb.api.getAccountState(addr).then(function (resp) {
		nonce = parseInt(resp.nonce || 0) + 1;
		neb.api.call({
			from: addr,
			to: config.contractAddr,
			value: 0,
			nonce: nonce,
			gasPrice: config.gasprice,
			gasLimit: config.gaslimit,
			contract: {
				"function": config.getSelfShareList,
				"args": ''
			}
		}).then(function (resp) {
			if(resp.execute_err==""){
				shares = JSON.parse(resp.result);
				personalShareDataDisplay();
			}
		}).catch(function (err) {
			console.log(err);
		});
	}).catch(function (e) {
		console.log(e);
	});
	
}
function getShareInfo(sid){
	return _.find(shares, function(o) { return o.id == sid; });
}
$(function(){
	getWallectInfo();
	$('#modal1').on('show.bs.modal', function (event) {
		  var target = $(event.relatedTarget);
		  var sid = target.data('sid') ;
		  initModal(target);
	});
});
function resetLocalWallet(){
	localStorage.wallet = "";
	window.location.href = 'personal.html';
}
var personalData = null;
function queryPersonalData(addr){
	neb.setRequest(new nebulas.HttpRequest(config.apiPrefix));
	neb.api.getAccountState(addr).then(function (resp) {
		nonce = parseInt(resp.nonce || 0) + 1;
		neb.api.call({
			from: addr,
			to: config.contractAddr,
			value: 0,
			nonce: nonce,
			gasPrice: config.gasprice,
			gasLimit: config.gaslimit,
			contract: {
				"function": config.account,
				"args": ''
			}
		}).then(function (resp) {
			if(resp.execute_err==""){
				personalData = JSON.parse(resp.result);
				console.log(personalData);
				personalDataDisplay();
			}else{
				tips('您还没有在平台发起拍卖，个人中心无数据，请点击发起拍卖。',false);
			}
		}).catch(function (err) {
			console.log(err);
		});
	}).catch(function (e) {
		console.log(e);
	});
}
//personalData
function personalDataDisplay(){
	$('.personalConfirm').hide();
	$('.personalDataContainer').removeClass('d-none');
	$('#p_wallet').text(personalData.wallet);
	$('#p_balance').text(new BigNumber(personalData.balance).div(1000000000000000000));
	initPersonalAcctlogDisplay();
}
function personalShareDataDisplay(){
	var personalShares = findPernoalShares();
	var reward = new BigNumber(0);
	var reply = new BigNumber(0);
	$.each(personalShares,function(index,share){
		reply = reply.plus(share.comments.length);
		$.each(share.profits,function(key,profit){
			reward = reward.plus(profit.value);
		});
	});
	$('#p_sharesNum').text(personalShares.length);
	$('#p_reward').text(reward);
	$('#p_reply').text(reply);
	
	initPersonalShareDisplay();
}
function findPernoalShares(){
	var personalShares = _.filter(shares, function(o) { return o.ownner == curWallet; });
	return personalShares;
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




function openTakeout(){
	var nas = new BigNumber(personalData.balance).div(1000000000000000000);
	var modal = $('#modal1')
	modal.find('.modal-title').text('提现');
	var html = [];
	html.push('<form class="takeout-form" novalidate><div class="form-group">');
	html.push('<label for="valueExp">提现金额(账户余额:'+nas+')</label>');
	html.push('<input type="text" class="form-control" id="takeoutvalue" aria-describedby="valueHelp" required>');
	html.push('<div class="invalid-feedback"> 请检查提现金额. </div>');
	html.push('</div></form>');
	html.push('<div class="row justify-content-md-center pt-2">');
	html.push('<div class="col col-sm-2 px-3 text-center">');
	html.push('<button type="button" class="btn btn-dark" onclick=sendTakeout();>确定提现</button>');
	html.push('</div></div>');
	modal.find('.modal-body').html('');
	modal.find('.modal-body').html(html.join(''));
	modal.modal('show');
}
function sendTakeout(){
	var forms = document.getElementsByClassName('takeout-form');
	var validation = Array.prototype.filter.call(forms, function(form) {
		if (form.checkValidity() === false) {
			event.preventDefault();
			event.stopPropagation();
		}else{
			var value = $('#takeoutvalue').val();
			var args = [value];
			defaultOptions.listener = function(data){
				if(typeof data === "object"){
					tips('提现发送成功，大约15秒后数据打包写入区块链后到账，请稍后刷新查看。',true);
				}else{
					tips(data,false);
				}
			};
			nebPay.call(config.contractAddr,"0",config.takeout,JSON.stringify(args),defaultOptions);
		}
		form.classList.add('was-validated');
	});
}
function initPersonalShareDisplay(target){
	var re = initShareDisplay(findPernoalShares(),'p_sharesContainer');
	if(re==false && target){
		$(target).text('No more');
	}
}
function initPersonalAcctlogDisplay(target){
	var re = initAccountLogsDisplay(personalData.logs,'acctlogContainer');
	if(re==false && target){
		$(target).text('No more');
	}
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
		html.push('<p class="media-body pb-1 mb-0 small lh-125 text-left">');
		html.push('<strong class="d-block text-gray-dark sharetitle" data-toggle="modal" data-target="#modal1" data-sid='+data[i].id+'>'+data[i].title+'</strong>');
		html.push(data[i].shareBody);
		html.push('</p>');
		html.push('</div>');
		html.push('<div class="text-muted media-body pb-1 mb-0 small lh-125 border-bottom border-gray">');
		html.push('<span class="d-block mt-2 text-right">');
		html.push('<i class="far fa-calendar-alt"></i><span id="createtime">'+new Date(data[i].createtime*1000).toLocaleString()+'</span>');
		html.push('<span class="reply" data-toggle="modal" data-target="#modal1" data-sid='+data[i].id+'><i class="far fa-comment-alt"></i>&nbsp;&nbsp;'+data[i].comments.length+'</span>');
		html.push('<span class="reward" data-toggle="modal" data-target="#modal1" data-sid='+data[i].id+'><i class="far fa-credit-card"></i>&nbsp;&nbsp;'+calcReward(data[i].profits)+'&nbsp;NAS</span>');
		var statusLabel = data[i].status=='enable'?'终止拍卖':'未拍卖';
		console.log(data[i].status);
		html.push('<span class="status" data-toggle="modal" data-target="#modal1" data-sid='+data[i].id+'><i class="fas fa-share-alt"></i>&nbsp;&nbsp;'+statusLabel+'</span>');
		html.push('<span class="editShare" data-toggle="modal" data-target="#modal1" data-sid='+data[i].id+'><i class="far fa-edit"></i>&nbsp;&nbsp;修改</span>');
		html.push('</span></div>');
	}
	$('.'+containerClass).append(html.join(''));
	Holder.run();
	return true;
}
function initAccountLogsDisplay(data,containerClass){
	$('.'+containerClass).find('.lodingdiv').remove();
	var displaySize = $('.'+containerClass).find('.media-body').length;
	var count = data.length;
	if(displaySize == count){return false}
	var loop = displaySize + pageSize;
	if(count  < (displaySize+pageSize)){
		loop = count;
	}
	var html = [];
	for(var i= displaySize;i<loop;i++){
		html.push('<div class="text-muted media-body pb-1 my-2 small lh-125 border-bottom border-gray">');
		html.push('<span class="d-block text-left">');
		html.push('<i class="far fa-calendar-alt"></i><span id="createtime" style="display: inline-block;width:120px;">'+new Date(data[i].time*1000).toLocaleString()+'</span>');
		var side = data[i].side == "save" ? "收到打赏" : "提现";
		html.push('<span class="text-center" style="display: inline-block;width:60px;">&nbsp;&nbsp;'+side+'</span>');
		html.push('&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-center" style="display: inline-block;width:100px;">&nbsp;&nbsp;'+new BigNumber(data[i].value).div(1000000000000000000)+'</span><small>NAS</small>');
		html.push('</span></div>');
	}
	$('.'+containerClass).append(html.join(''));
	return true;
}
function initModal(target){
	if(target.hasClass('sharetitle')){
		showShareInfoInModal(target.data('sid'));
	}else  if(target.hasClass('reply')){
		showShareInfoInModal(target.data('sid'));
	}else if(target.hasClass('reward')){
		showRewardInModal(target.data('sid'));
	}else if(target.hasClass('status')){
		resetShareStatus(target.data('sid'));
	}else if(target.hasClass('editShare')){
		editShare(target.data('sid'));
	}
}
function showShareInfoInModal(sid){
	var share = getShareInfo(sid);
	comments = share.comments.reverse();
	var modal = $('#modal1')
	modal.find('.modal-title').text('查看拍卖内容');
	var html = [];
	html.push('<p class="text-lg-center">'+share.title+'</p>');
	html.push('<p class="text-center text-gray-dark small text-muted">作者：'+ share.ownner +" 发布时间："+ new Date(share.createtime*1000).toLocaleString()+'</p>');
	html.push('<span class="text-md-left text-muted">'+share.shareBody+'</span>');
	//reply
	html.push('<div class="container shareReplys"></div>');
	modal.find('.modal-body').html('');
	modal.find('.modal-body').html(html.join(''));
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
var profits = [];
function showRewardInModal(sid){
	var share = getShareInfo(sid);
	profits = share.profits.reverse();
	var modal = $('#modal1')
	modal.find('.modal-title').text('查看打赏记录');
	var html = [];
	html.push('<p class="text-lg-center">'+share.title+'</p>');
	html.push('<p class="text-center text-gray-dark small text-muted">作者：'+ share.ownner +" 发布时间："+ new Date(share.createtime*1000).toLocaleString()+'</p>');
	html.push('<span class="text-md-left text-muted">'+share.shareBody+'</span>');
	html.push('<p class="text-muted media-body pb-1 my-1  border-bottom border-gray">打赏记录</p>');
	//reply	
	html.push('<div class="container shareProfits px-0"></div>');
	modal.find('.modal-body').html('');
	modal.find('.modal-body').html(html.join(''));
	genShareProfits(0);
}
function genShareProfits(page){
	var size = 5;	
	var len = profits.length;
	var loop = (size * page + size)>len ?  len : size * page + size;
	var html = [];
	for(var i=size * page;i<loop;i++){
		var color = randomColor();
		html.push('<div class="text-muted media-body pb-1 my-2 small lh-125 border-bottom border-gray">');
		html.push('<span class="d-block text-left">');
		html.push('<i class="far fa-calendar-alt"></i><span id="createtime">'+new Date(profits[i].time*1000).toLocaleString()+'</span>');
		html.push('<i class="far fa-user-circle"></i><span>&nbsp;&nbsp;'+profits[i].from+'</span>');
		html.push('&nbsp;&nbsp;&nbsp;&nbsp;<i class="fas fa-hand-holding-usd"></i><span>&nbsp;&nbsp;'+profits[i].value+'</span><small>NAS</small>');
		html.push('</span></div>');
	}
	html.push('<div class="row text-muted mt-2 justify-content-md-center">');
	if(page == 0 && len>(size * page + size)){
		html.push('<button type="button" class="btn btn-secondary m-1" onclick=genShareProfits('+(page+1)+')>下一页</button>');
	}else if(page != 0 && (size * page + size)>=len){
		html.push('<button type="button" class="btn btn-secondary m-1" onclick=genShareProfits('+(page-1)+')>上一页</button>');
	}else if(page != 0 && (size * page + size) < len){
		html.push('<button type="button" class="btn btn-secondary m-1" onclick=genShareProfits('+(page-1)+')>上一页</button>');
		html.push('<button type="button" class="btn btn-secondary m-1" onclick=genShareProfits('+(page+1)+')>下一页</button>');
	}
	html.push('</div>');
	$('.shareProfits').html('');
	$('.shareProfits').html(html.join(''));
	Holder.run();
}
function resetShareStatus(sid){
	var share = getShareInfo(sid);
	var modal = $('#modal1')
	modal.find('.modal-title').text('状态设置');
	var html = [];
	html.push('<p class="text-lg-center">'+share.title+'</p>');
	html.push('<p class="text-center text-gray-dark small text-muted">作者：'+ share.ownner +" 发布时间："+ new Date(share.createtime*1000).toLocaleString()+'</p>');
	html.push('<span class="text-md-left text-muted">'+share.shareBody+'</span>');
	if(share.status == 'enable'){
		html.push('<div class="row mt-3 justify-content-md-center"><button type="button" class="btn btn-danger m-1" onclick=resetShareStatusAction("'+sid+'","disable");>停止拍卖</button></div>');
	}else{
		html.push('<div class="row mt-3 justify-content-md-center"><button type="button" class="btn btn-secondary m-1" onclick=resetShareStatusAction("'+sid+'","enable");>开启拍卖</button></div>');
	}
	modal.find('.modal-body').html('');
	modal.find('.modal-body').html(html.join(''));
}
function resetShareStatusAction(sid,status){
	var value = $('#takeoutvalue').val();
	var args = [{id:sid,status:status}];
	defaultOptions.listener = function(data){
		if(typeof data === "object"){
			tips('调整操作发送成功，大约15秒后数据打包写入区块链后完成状态修改，请稍后刷新查看。',true);
		}else{
			tips(data,false);
		}
	};
	nebPay.call(config.contractAddr,"0",config.resetShareStatus,JSON.stringify(args),defaultOptions);
}
function editShare(sid){
	var share = getShareInfo(sid);
	var modal = $('#modal1')
	modal.find('.modal-title').text('修改内容');
	var html = [];
	html.push('<div class="alert alert-warning px-3 text-center small">');
	html.push('<i class="fas fa-exclamation-triangle"></i>发布信息请遵守当地法律法规！');
	html.push('</div>');
	html.push('<form class="editshare-form" novalidate><div class="form-group">');
	html.push('<label for="exampleInputEmail1">主题</label>');
	html.push('<input type="hidden" class="form-control" id="editshareId" aria-describedby="shareIdHelp" value='+share.id+'>');
	html.push('<input type="text" class="form-control" id="editshareTitle" aria-describedby="shareTitleHelp" value='+share.title+' required>');
	html.push('<div class="invalid-feedback"> 请输入主题. </div>');
	html.push('</div>');
	html.push('<div class="form-group">');
	html.push('<label for="shareContentlabel">拍卖内容</label>');
	html.push('<textarea class="form-control" rows=5 id="editshareContent" required>'+share.shareBody+'</textarea>');
	html.push('<div class="invalid-feedback"> 请输入拍卖内容. </div>');
	html.push('</div></form>');
	html.push('<div class="row justify-content-md-center pt-2">');
	html.push('<div class="col col-sm-2 px-3 text-center">');
	html.push('<button type="button" class="btn btn-dark" onclick=editShareAction();>确认修改</button>');
	html.push('</div></div>');
	modal.find('.modal-body').html('');
	modal.find('.modal-body').html(html.join(''));
	modal.modal('show');
}
function editShareAction(){
	var forms = document.getElementsByClassName('editshare-form');
	var validation = Array.prototype.filter.call(forms, function(form) {
		if (form.checkValidity() === false) {
			event.preventDefault();
			event.stopPropagation();
		}else{
			var id = $('#editshareId').val();
			var title = $('#editshareTitle').val();
			var shareContent = $('#editshareContent').val();
			var args = [{id:id,title:title,shareBody:shareContent}];
			defaultOptions.listener = function(data){
				if(typeof data === "object"){
					tips('修改成功，大约15秒后数据打包写入区块链，请稍后刷新查看。',true);
				}else{
					tips(data,false);
				}
			};
			nebPay.call(config.contractAddr,"0",config.editShare,JSON.stringify(args),defaultOptions);
		}
		form.classList.add('was-validated');
	});
}

