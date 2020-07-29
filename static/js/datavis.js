/**
 * 数据可视化，2017-08-15
 */


// 使用ajax获取动态数据
function myrequest()
{
	$.ajax({
		url: '/datavis/gethp',
		type: 'GET',
		async: false,
		data: {},
		dataType: 'json',
		cache: false,
		timeout: 3000,
		//beforeSend: function(){$("#ntfText").html("loading。。。");},
		success: function(result) {
			$("#ntfText").html(fmoney(result.P_stat_hpuser_alluser));
		}
	});
}
//数字格式转换：整型
function fmoney(s) {
	//n = n > 0 && n <= 20 ? n : 0;
	n=0;
	s = parseFloat((s + "").replace(/[^\d\.-]/g, "")).toFixed(n) + "";
	var l = s.split(".")[0].split("").reverse();
	t = "";
	for (i = 0; i < l.length; i++) {
	t += l[i] + ((i + 1) % 3 == 0 && (i + 1) != l.length ? "," : "");
	}
	return t.split("").reverse().join("");
}

//数据格式转换：小数点
function fmoney2(s, n) {
	n = n > 0 && n <= 20 ? n : 2;
	s = parseFloat((s + "").replace(/[^\d\.-]/g, "")).toFixed(n) + "";
	var l = s.split(".")[0].split("").reverse(), r = s.split(".")[1];
	t = "";
	for (i = 0; i < l.length; i++) {
	t += l[i] + ((i + 1) % 3 == 0 && (i + 1) != l.length ? "," : "");
	}
	return t.split("").reverse().join("") + "." + r;
}