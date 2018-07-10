'use strict';
// 定义信息类
var Share = function(obj) {
	if (typeof obj === "string") {
		obj = JSON.parse(obj);
	}
	if (typeof obj === "object") {
		this.id = obj.id;
		this.ownner = obj.ownner;//wallet addr
		this.title = obj.title;
		this.shareBody = obj.shareBody;
		this.createtime = obj.createtime;
		this.comments = obj.comments;
		this.profits = obj.profits;
		this.status = obj.status;//enable disable
	} else {
		this.id = "";
		this.ownner = "";//wallet addr
		this.title = "";
		this.shareBody = "";
		this.createtime = "";
		this.comments = [];
		this.profits = [];
		this.status = "";
	}
};

// 将信息类对象转成字符串
Share.prototype = {
	toString : function() {
		return JSON.stringify(this);
	},
	addComment : function(comment) {
		if (this.comments == null) {
			this.comments = [];
		}
		if (typeof comment != "undefined") {
			this.comments.push(comment);
		}
	},
	addProfit : function(profit) {
		if (this.profits == null) {
			this.profits = [];
		}
		if (typeof profit != "undefined") {
			this.profits.push(profit);
		}
	}
};
//comment 
var Comment = function(obj) {
	if (typeof obj === "string") {
		obj = JSON.parse(obj)
	}
	if (typeof obj === "object") {
		this.wallet = obj.wallet;
		this.name = obj.name;
		this.text = obj.text;
		this.time = obj.time;
	} else {
		this.wallet = "";
		this.name = "";
		this.text = "";
		this.time = "";
	}
};
Comment.prototype = {
	toString : function() {
		return JSON.stringify(this);
	}
};
//Reward 
var Reward = function(obj) {
	if (typeof obj === "string") {
		obj = JSON.parse(obj)
	}
	if (typeof obj === "object") {
		this.from = obj.from;
		this.value = obj.value;
		this.time = obj.time;
	} else {
		this.from = "";
		this.value = "";
		this.time = "";
	}
};
Reward.prototype = {
	toString : function() {
		return JSON.stringify(this);
	}
};

var Account = function(obj) {
	if (typeof obj === "string") {
		obj = JSON.parse(obj)
	}
	if (typeof obj === "object") {
		this.wallet = obj.wallet;
		this.balance = obj.balance;
		this.logs = obj.logs;
	} else {
		this.wallet = "";
		this.balance = new BigNumber(0);
		this.logs = [];
	}
};
Account.prototype = {
	toString : function() {
		return JSON.stringify(this);
	},
	addLog : function(log) {
		if (this.logs == null) {
			this.logs = [];
		}
		if (typeof log != "undefined") {
			this.logs.push(log);
		}
	}
};
var AccountLog = function(obj) {
	if (typeof obj === "string") {
		obj = JSON.parse(obj)
	}
	if (typeof obj === "object") {
		this.side = obj.side;// save or takeout
		this.value = obj.value;
		this.time = obj.time;
	} else {
		this.side = "";
		this.value = new BigNumber(0);
		this.time = 0;
	}
};
AccountLog.prototype = {
	toString : function() {
		return JSON.stringify(this);
	}
};

//根据官方的API来创建存储空间
var ShareResourceContract = function() {
	LocalContractStorage.defineProperties(this, {
		_name : null,
		_creator : null,
		_balance : new BigNumber(0),
		_fee : new BigNumber(0.01),
		_wei : 1000000000000000000,
		_index : 0
	});
// 使用内置的LocalContractStorage绑定一个map
	LocalContractStorage.defineMapProperties(this, {
		"shares" : {
			parse : function(value) {
				return new Share(value);
			},
			stringify : function(o) {
				return o.toString();
			}
		},
		"shareKeys" : {
			parse : function(value) {
				return value.toString();
			},
			stringify : function(o) {
				return o.toString();
			}
		},
		"accts" : {
			parse : function(text) {
				return new Account(text);
			},
			stringify : function(o) {
				return o.toString();
			}
		}
	});
};

ShareResourceContract.prototype = {
	init : function() {
		this._name = "Nebulas ShareResourceContract. author:n1UipJY7CjHa25FBtz2drnC79WTgd2YejzH";
		this._creator = Blockchain.transaction.from;
		this._balance = new BigNumber(0);
		this._fee = new BigNumber(0.01);
		this._wei = 1000000000000000000;
		this._index = 0;
	},

	name : function() {
		return this._name;
	},
	
	ownner : function() {
		return this._creator;
	},
	
	resetOwnner: function(addr) {
		if(this._creator === Blockchain.transaction.from && this.verifyAddress(addr)){
			this._creator = addr;
		}else{
			return 'Permission denied!';
		}
	},
	
	wei : function() {
		return this._wei;
	},
	
	resetWei : function(wei) {
		if(this._creator === Blockchain.transaction.from){
			this._wei = wei;
		}else{
			return 'Permission denied!';
		}
	},
	
	fee: function() {
		return this._fee;
	},
	
	resetFee: function(value) {
		if(this._creator === Blockchain.transaction.from){
			this._fee = new BigNumber(value);
		}else{
			return 'Permission denied!';
		}
	},
	
	balanceOfContract : function() {
		if(this._creator === Blockchain.transaction.from){
			return this._balance;
		}else{
			return 'Permission denied!';
		}
	},
	
	account : function() {
		var from = Blockchain.transaction.from;
		var acct = this.accts.get(from);
		if(acct){
			return acct;
		}else{
			throw new Error("No account before.");
		}
	},
	
	balanceOf : function() {
		var from = Blockchain.transaction.from;
		var acct = this.accts.get(from);
		if(acct){
			return acct.balance;
		}else{
			throw new Error("No account before.");
		}
	},
	
	
	_save : function(address) {
		if(this.verifyAddress(address)){
			var value = Blockchain.transaction.value;
			if(value.gt(new BigNumber(0))){
				this._balancePlus(value,address);
			}else{
				throw new Error("A reward must be greater than zero.");
			}
		}else{
			return 'Address['+address+'] invalid!';
		}
	},
	
	_balancePlus:function(value,address){
		var percent = new BigNumber(1).sub(this._fee);
		var toUser = value.mul(percent);
		var acct = this.accts.get(address);
		var log = new AccountLog({
			side : "save",// save or takeout
			value : toUser,
			time : Blockchain.transaction.timestamp.toString(10)
		});
		if(!acct){
			var tmp = new Account({
				wallet : address,
				balance : toUser,
				logs : []
			});
			tmp.addLog(log);
			this.accts.set(address,tmp);
		}else{
			acct.balance = new BigNumber(acct.balance).plus(toUser);
			acct.addLog(log);
			this.accts.set(address,acct);
		}
		this._balance = value.plus(this._balance);
	},
	
	takeout : function(value) {
		var from = Blockchain.transaction.from;
		var amount = new BigNumber(value).mul(this._wei);

		var acct = this.accts.get(from);
		if (!acct) {
			throw new Error("No account before.");
		}

		if (amount.gt(acct.balance)) {
			throw new Error("Insufficient balance.");
		}

		var result = Blockchain.transfer(from, amount);
		if (!result) {
			throw new Error("transfer failed.");
		}
		
		this._balance = new BigNumber(this._balance).sub(amount);
		
		var log = new AccountLog({
			side : "takeout",// save or takeout
			value : amount,
			time : Blockchain.transaction.timestamp.toString(10)
		});
		acct.addLog(log);
		acct.balance = new BigNumber(acct.balance).sub(amount);
		this.accts.set(from,acct);
	},
	
	withdraw: function(address,value) {
		var amount = new BigNumber(value).mul(this._wei);
		if (amount.gt(new BigNumber(this._balance))) {
			throw new Error("Insufficient balance of Contract["+this._balance+"].");
		}
		
		if(this._creator === Blockchain.transaction.from && this.verifyAddress(address)){
			var result = Blockchain.transfer(address, amount);
			if(result){
				this._balance = new BigNumber(this._balance).sub(amount);
			}else{
				throw new Error("Withdraw error.");
			}
		}else{
			return 'Permission denied or address invalid!';
		}
	},

	verifyAddress : function(address) {
		// 1-valid, 0-invalid
		var result = Blockchain.verifyAddress(address);
		return {
			valid : result == 0 ? false : true
		};
	},
	
	share : function(args) {
		var arg = new Share(args);
		var from = Blockchain.transaction.from;
		var time = Blockchain.transaction.timestamp.toString(10);
		var shareid = from + time;
		var share = new Share({
			id : shareid,
			ownner : from,
			title : arg.title,
			shareBody : arg.shareBody,
			createtime : time,
			comments : [],
			profits : [],
			status : "enable"
		});
		this._index ++;
		this.shareKeys.set(this._index,shareid);
		this.shares.set(shareid,share);
		//init acct
		var acct = this.accts.get(from);
		if(!acct){
			var tmp = new Account({
				wallet : from,
				balance : new BigNumber(0),
				logs : []
			});
			this.accts.set(from,tmp);
		}
	},
	editShare : function(args) {
		var arg = new Share(args);
		var from = Blockchain.transaction.from;
		var share = this.shares.get(arg.id);
		
		if(!share){
			throw new Error("No sharing based on:"+shareid);
		}
		
		if(from != share.ownner){
			throw new Error("Only ownner can be edit.");
		}
		share.title = arg.title;
		share.shareBody = arg.shareBody;
		this.shares.set(arg.id,share);
	},
	
	resetShareStatus : function(args) {
		var arg = new Share(args);
		var from = Blockchain.transaction.from;
		var share = this.shares.get(arg.id);
		
		if(!share){
			throw new Error("No sharing based on:"+shareid);
		}
		
		if(from != share.ownner){
			throw new Error("Only ownner can be edit.");
		}
		
		if(typeof args.status != 'undefined' && args.status == 'enable'){
			share.status = "enable";
		}else{
			share.status = "disable";
		}
		this.shares.set(arg.id,share);
	},
	
	reply : function(shareid,args) {
		var arg = new Comment(args);
		var from = Blockchain.transaction.from;
		
		var share = this.shares.get(shareid);
		if(!share){
			throw new Error("No sharing based on:"+shareid);
		}
		
		var comment = new Comment({
			wallet : from,
			name : arg.name,
			text : arg.text,
			time : Blockchain.transaction.timestamp.toString(10)
		});
		
		share.addComment(comment);
		this.shares.set(shareid,share);
	},
	
	reward : function(shareid) {
		var share = this.shares.get(shareid);
		if(!share){
			throw new Error("No sharing based on:"+shareid);
		}
		
		var reward = new Reward({
			from : Blockchain.transaction.from,
			value : Blockchain.transaction.value.div(this._wei),
			time : Blockchain.transaction.timestamp.toString(10)
		});
		
		share.addProfit(reward);
		this.shares.set(shareid,share);
		this._save(share.ownner);
	},
	
	getShareList:function(){
		var list = [];
    	for(var i=1;i<=this._index;i++){
    		var key = this.shareKeys.get(i);
    		var share = this.shares.get(key);
    		if(share.status === 'enable'){
    			list.push(share);
    		}
    	}
        return list;
	},
	
	getSelfShareList:function(){
		var list = [];
		var form = Blockchain.transaction.from;
		for(var i=1;i<=this._index;i++){
			var key = this.shareKeys.get(i);
			var share = this.shares.get(key);
			if(share.ownner === form){
				list.push(share);
			}
		}
		return list;
	},
	
	search:function(keyWord){
		var reg = new RegExp(keyWord);
		var list = [];
		for(var i=1;i<=this._index;i++){
			var key = this.shareKeys.get(i);
			var share = this.shares.get(key);
			if(share.status === 'enable' 
				&& ( share.title.match(reg) || share.shareBody.match(reg) ) ){
				list.push(share);
			}
		}
		return list;
	}
};
module.exports = ShareResourceContract; //合约标识接口 执行ShareResourceContract