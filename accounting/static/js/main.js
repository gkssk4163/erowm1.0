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

String.prototype.number = function() {
	var num = this.replace(/[^0-9]/g, "");
	return num;
}

Number.prototype.number = String.prototype.number;

function initDatepickerByClass() {
	var options = {
		'changeMonth': true,
		'changeYear': true,
		dateFormat: 'yy-mm-dd'
	};

	$.each(arguments, function(index, value) {
		$(document).find("." + value).removeClass("hasDatepicker").datepicker(options);
	});
}

/*function initStartEndDatepicker(startDateElementId, endDateElementId) {
	var startDatepicker = $("#" + startDateElementId);
	var endDatepicker = $("#" + endDateElementId);
	console.log(endDatepicker.val());
	console.log(startDatepicker.val());

	var startDatePickerOptions = {
		'changeMonth': true,
		'changeYear': true,
		'maxDate': endDatepicker.val(),
		'onClose': function(datepicker) {
			endDatepicker.datepicker('option', 'minDate', datepicker);
		}
	};

	var endDatePickerOptions = {
		'changeMonth': true,
		'changeYear': true,
		'minDate': startDatepicker.val(),
		'onClose': function(datepicker) {
			startDatepicker.datepicker('option', 'maxDate', datepicker);
		}
	};

	startDatepicker.datepicker(startDatePickerOptions);
	endDatepicker.datepicker(endDatePickerOptions);
}*/

// 회계년도 구하기
function getSessionYear(business, startDate) {
	if (business == "어린이집") {
		if (moment(startDate).format("M") < 3) {
			return moment(startDate).format("YYYY") - 1;
		}
	}

	return moment(startDate).format("YYYY");
}

function ChkIsEmpty(str) {
	if (str == null) return "";
	if (str == "NaN") return "";
	if (new String(str).valueOf() == "undefined") return "";
	var chkStr = new String(str);
	if( chkStr.valueOf() == "undefined" ) return "";
	if (chkStr == null) return "";
	if (chkStr.toString().length == 0 ) return "";
	return str;
}

function ChkIsNull(str) {
	if (str == null) return true;
	if (str == "NaN") return true;
	if (new String(str).valueOf() == "undefined") return true;
	var chkStr = new String(str);
	if( chkStr.valueOf() == "undefined" ) return true;
	if (chkStr == null) return true;
	if (chkStr.toString().length == 0 ) return true;
	return false;
}