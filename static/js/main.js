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

