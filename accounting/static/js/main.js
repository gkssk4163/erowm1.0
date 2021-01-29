function cancelCheck()
{
	if(confirm('정말 취소하시겠습니까?'))
	{
		history.back();
	}
}

jQuery.fn.hideTableRow = function() {
	$tr = this;
	$tr.children('td').wrapInner('<div style="display: none;" />');
	$tr.hide();
	return $tr;
};

jQuery.fn.slideFadeTableRow = function(speed, easing, callback) {
	$tr = this;
	if ($tr.is(':hidden')) {
		$tr.show().find('td > div').animate({opacity: 'toggle', height: 'toggle'}, speed, easing, callback);
	}
	return $tr;
};

String.prototype.left = function(len) {
	if (this.length == 0 || this.length < len) return this;
	return this.substring(0, len);
}

String.prototype.right = function(len) {
	if (this.length == 0 || this.length < len) return this;
	return this.substring(this.length - len, this.length);
}

String.prototype.comma = function(gubn) {
	var num = this.toString().split(".");
	num[0] = num[0].replace(/[^0-9]/g, "");
	if(num[1]) {
		num[1] = num[1].replace(/[^0-9]/g, "");
	}
	
	if (this.toString().trim().left(1) != "-") {
		if(num[0].length == 0 || isNaN(num[0])) return "";
	}
	
	var positive = num[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
	if (this.toString().trim().left(1) == "-") {
		positive = "-" + positive;
	}
	
	if(gubn) {
		gubn = gubn.replace(/[^0-9]/g, "");	
		
		if(typeof num[1] == "undefined") {
			return positive;
		}
		else if(num[1] == "") {
			positive = positive + ".";
		}
		else {
			positive = positive + "." + (num[1] + "000").substring(0, (num[1].length < gubn ? num[1].length : gubn));
		}
	}
	
	return positive;
}

Number.prototype.comma = String.prototype.comma;