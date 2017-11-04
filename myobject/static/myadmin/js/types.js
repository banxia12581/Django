
/*types-edit 页面--------------------------------------------------*/
//商品类别加正则判断
function addTypeVerify(){
	var tnameOk=false;
	var tpidOk=false;
	//商品类别名丧失焦点事件
	$('input[name=typesname]').blur(function(){
		//获取商品类别名进行正则获取
		var v =$(this).val();
		var reg=/^[\u4E00-\u9FA5\uF900-\uFA2D\s\w]{1,32}$/;
		//判断如果为true则通过
		if(reg.test(v)){
		             $(this).css('border-color','#52a8ec');
		             $('#tnameVerify').addClass('hidden');
		             tnameOk=true;
		}else{
		                $(this).css('border-color','#d80000');
		                $('#tnameVerify').removeClass('hidden');
		                $('#tnameVerify').html("请输入格式正确的商品类别名称")
		                tnameOk=false;
		}
	})
	//商品父类id丧失焦点事件
	$('input[name=typespid]').blur(function(){
		//获取商品父类id进行正则获取
		var v =$(this).val();
		var reg=/^[\u4E00-\u9FA5\uF900-\uFA2D\s\w]{1,255}$/;
		//判断如果为true则通过
		if(reg.test(v)){
		             $(this).css('border-color','#52a8ec');
		             $('#tidVerify').addClass('hidden');
		             tnameOk=true;
		}else{
		             $(this).css('border-color','#d80000');
		             $('#tidVerify').removeClass('hidden');
		             $('#tidVerify').html("请输入格式正确的商品父类ID")
		             tnameOk=false;
		}
	})
}

/*---------------------------------------------------------------------*/

/*users-add 页面--------------------------------------------------*/


/*---------------------------------------------------------------------*/