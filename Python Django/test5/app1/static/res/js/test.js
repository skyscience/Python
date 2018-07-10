'use strict';
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
var BankContract = function() {
	LocalContractStorage.defineProperties(this, {
		_name : null,
		_creator : null,
		_balance : new BigNumber(0),
		_fee : new BigNumber(0.01),
		_wei : 1000000000000000000,
		_index : 0
	});

	LocalContractStorage.defineMapProperties(this, {
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

TestContract.prototype = {
	init : function() {
		this._name = "Nebulas BankContract.";
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
	
	balanceOf : function() {
		var from = Blockchain.transaction.from;
		var acct = this.accts.get(from);
		if(acct){
			return acct.balance;
		}else{
			throw new Error("No account before.");
		}
	},
	
	save : function(address) {
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
		this._balance = value.plus(this._balance);
		
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
			var tmp = this.accts.get(address);
			tmp.balance = tmp.balance.plus(toUser);
			this.accts.set(address,tmp);
		}
	},
	
	takeout : function(value) {
		var from = Blockchain.transaction.from;
		var amount = new BigNumber(value).mul(this._wei);

		var acct = this.accts.get(from);
		if (!acct) {
			throw new Error("No deposit before.");
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
	}
};
module.exports = BankContract;