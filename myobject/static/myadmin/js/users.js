
/*base 页面--------------------------------------------------*/
//左侧导航切换选中
function leftNav(){
	var urlstr = location.href;  
  	var urlstatus=false;  
  	var t = urlstr.split('/');
  	var tLength = t.length;
  	$(".level a").each(function () {  
   		if ((urlstr).indexOf($(this).attr('href')) > -1&&$(this).attr('href')!="") {  
      			$(this).parent('li').addClass('active'); 
      			$(".level a").eq(0).parent('li').removeClass('active');
      			$(".level a").eq(3).parent('li').removeClass('active');
      			urlstatus = true;  
   		} else if(t[tLength-1] == ''){
   			$(".level a").eq(0).parent('li').addClass('active');
   		}else if (t[tLength-1] == 'types'){
   			$(".level a").eq(3).parent('li').addClass('active');
   		}
   		else{  
      			$(this).parent('li').removeClass('active');
    		}  
  	});  
}

/*base 页面 E--------------------------------------------------*/
/*users-index 页面--------------------------------------------------*/
//列表中的性别和状态将数字显示为中文
function stateChange(){
	var trLisr = $('tbody tr');
	var i =0;
	while(i < trLisr.length){
		var sext= $('tbody tr').eq(i).find('.userSex').text();
		var statet = $('tbody tr').eq(i).find('.userState').text();
		if(sext == 0){
			$('tbody tr').eq(i).find('.userSex').text('女');
		}else if(sext == 1){
			$('tbody tr').eq(i).find('.userSex').text('男');
		}
		if(statet == 0){
			$('tbody tr').eq(i).find('.userState').text('后台管理员');
		}else if(statet == 1){
			$('tbody tr').eq(i).find('.userState').text('启用');
		}else if(statet == 2){
			$('tbody tr').eq(i).find('.userState').text('禁用');
		}
		i++;
		console.log(sext)
	}
}
/*---------------------------------------------------------------------------*/
/*users-edit 页面--------------------------------------------------*/

//性别默认选中状态
function sexState(){
	var sexChoice = $('#sexChoice').val();
	if(sexChoice == 1){
		$("#man").prop("checked", true);
	}else{
		$('#woman').prop("checked", true);
	}
}

//用户状态默认选中状态
function stateState(){
	var stateChoice = $('#stateChoice').val();
	if(stateChoice == 1){
		$("#stateOpen").prop("checked", true);
	}else if(stateChoice == 2){
		$('#stateClose').prop("checked", true);
	}else{
		$('#stateAdmin').prop("checked", true);
	}
}
/*---------------------------------------------------------------------*/

/*users-add 页面--------------------------------------------------*/
//用户名判断未实现
function userName(){
	var unItem = $('.unItem');
	var uniText = $('.unItem').text();
	var unInput = $('input[name=username]').val();
	for(var i = 0;i<unItem.length;i++){
		if (unInput ==  uniText){
			alert("用户名重复,请更换!");
		}
	}	
}

//用户添加正则判断
function addUsersVerify(){
	//   提交
	var nameOk=false;
	var unameOk=false;
	var passOk=false;
	var repassOk=false;
	var phoneOk=false;
	var emailOk=false;
	var codeOk=false;
	var addressOk=false;
	//用户名丧失焦点事件
	$('input[name=username]').blur(function(){
		//获取用户信息进行正则获取
		var v =$(this).val();
		var reg=/^\w{4,32}$/;
		//判断如果为true则通过
		if(reg.test(v)){
	                	$(this).css('border-color','#52a8ec');
	                	$('#unameVerify').addClass('hidden');
	                	unameOk=true;
		}else{
	                	$(this).css('border-color','#d80000');
	                	$('#unameVerify').removeClass('hidden');
	                	$('#unameVerify').html("请输入格式正确的用户名")
	                	unameOk=false;
		}
	})
	//真实姓名丧失焦点事件
	$('input[name=name]').blur(function(){
		//获取真实姓名进行正则获取
		var v =$(this).val();
		var reg=/^[\u4E00-\u9FA5\uF900-\uFA2D\w]{1,16}$/;
		//判断如果为true则通过
		if(reg.test(v)){
	                	$(this).css('border-color','#52a8ec');
	                	$('#nameVerify').addClass('hidden');
	                	nameOk=true;
		}else{
	                	$(this).css('border-color','#d80000');
	                	$('#nameVerify').removeClass('hidden');
	                	$('#nameVerify').html("请输入格式正确的真实姓名")
	                	nameOk=false;
		}
	})
	//密码丧失焦点事件
	$('input[name=passwd]').blur(function(){
	            //获取密码
	            var v =$(this).val();
	            var reg=/^\w{6,32}$/;
	            //判断如果为true则通过
	            if(reg.test(v)){
			$(this).css('border-color','#52a8ec');
			$('#passVerify').addClass('hidden');
			passOk=true;
	            }else{
		    	$(this).css('border-color','#d80000');
		    	$('#passVerify').removeClass('hidden');
		    	$('#passVerify').html("请输入格式正确的密码")
		    	passOk=false;
	            }
	})
	//重复密码丧失焦点事件
	$('input[name=repasswd]').blur(function(){
	            //获取重复密码
	            var v =$(this).val();
	            var reg=/^\w{6,32}$/;
	            //判断如果为true则通过
	            if(reg.test(v)){
			$(this).css('border-color','#52a8ec');
			$('#repassVerify').addClass('hidden');
			repassOk=true;
	            }else{
		    	$(this).css('border-color','#d80000');
		    	$('#repassVerify').removeClass('hidden');
		    	$('#repassVerify').html("请输入格式正确的密码")
		    	repassOk=false;
	            }
	})
	//手机号丧失焦点事件
	$('input[name=phone]').blur(function(){
	            //获取手机号
	            var v =$(this).val();
	            var reg=/^\w{6,16}$/;
	            //判断如果为true则通过
	            if(reg.test(v)){
			$(this).css('border-color','#52a8ec');
			$('#phoneVerify').addClass('hidden');
			phoneOk=true;
	            }else{
		    	$(this).css('border-color','#d80000');
		    	$('#phoneVerify').removeClass('hidden');
		    	$('#phoneVerify').html("请输入格式正确的手机号")
		    	phoneOk=false;
	            }
	})
	//邮箱丧失焦点事件
	$('input[name=email]').blur(function(){
	            //获取邮箱
	            var v =$(this).val();
	            var reg=/^\w+@\w+\.(com|cn|org|net)$/;
	            //判断如果为true则通过
	            if(reg.test(v)){
			$(this).css('border-color','#52a8ec');
			$('#emailVerify').addClass('hidden');
			emailOk=true;
	            }else{
		    	$(this).css('border-color','#d80000');
		    	$('#emailVerify').removeClass('hidden');
		    	$('#emailVerify').html("请输入格式正确的邮箱")
		    	emailOk=false;
	            }
	})
	//邮编丧失焦点事件
	$('input[name=code]').blur(function(){
	            //获取邮编
	            var v =$(this).val();
	            var reg=/^\w{0,6}$/;
	            //判断如果为true则通过
	            if(reg.test(v)){
			$(this).css('border-color','#52a8ec');
			$('#codeVerify').addClass('hidden');
			codeOk=true;
	            }else{
		    	$(this).css('border-color','#d80000');
		    	$('#codeVerify').removeClass('hidden');
		    	$('#codeVerify').html("请输入格式正确的邮编")
		    	codeOk=false;
	            }
	})
	//地址丧失焦点事件
	$('input[name=address]').blur(function(){
	            //获取地址
	            var v =$(this).val();
	            var reg=/^[\u4E00-\u9FA5\uF900-\uFA2D\s\w]{0,255}$/;
	            //判断如果为true则通过
	            if(reg.test(v)){
			$(this).css('border-color','#52a8ec');
			$('#addressVerify').addClass('hidden');
			addressOk=true;
	            }else{
		    	$(this).css('border-color','#d80000');
		    	$('#addressVerify').removeClass('hidden');
		    	$('#addressVerify').html("请输入格式正确的地址")
		    	addressOk=false;
	            }
	})
}

/*---------------------------------------------------------------------*/
/*订单详情展示页-----------------------------*/ 

//按钮点击订单状态修改
function detailStatChange(){
	//发送ajax请求
	function doajax(ostatus,oid){
		$.ajax({
			url: "/myadmin/detailstatus",
			type: 'GET',
			dataType: 'json',
			data:{'ostatus':ostatus,'oid':oid},
			error:function() {
				alert("ajax加载失败！");
			},
		})
	}
	var jVerify = $('#J_verify');
	var jCancel = $('#J_cancel');
	$('#J_verify').click(function(){
		var ostatus = $('input[name=statuschange]').val();
		ostatus = 1;
		$('.ostate').text('已发货');
		var oid = $('input[name=orderid]').val();
		$('input[name=statuschange]').val(ostatus);
		doajax(ostatus,oid);

	});
	$('#J_cancel').click(function(){
		var ostatus = $('input[name=statuschange]').val()
		ostatus = 3;
		$('.ostate').text('无效订单');
		var oid = $('input[name=orderid]').val();
		$('input[name=statuschange]').val(ostatus);
		doajax(ostatus,oid);

	});
}

/*---------------------------------------------------*/ 

/*types-index---------------------------------------------*/ 
//分类展示商品类别
function typeShow(){
	var trList = $('.tbodyfir tr');
	for(var i =0;i<trList.length;i++){
		var pgid = $('.tbodyfir tr').eq(i).attr('pgid');
		var pid = $('.tbodyfir tr').eq(i).attr('pid');
		// 默认显示手机类
		if(pid==1|| pgid ==1){
			$('.tbodyfir tr').eq(i).removeClass('hidden')
		}else{
			$('.tbodyfir tr').eq(i).addClass('hidden')
		}
	}
	$('thead .typeid').click(function() {
		var parTr = $(this).val();
		for(var i =0;i<trList.length;i++){
			var pgid = $('.tbodyfir tr').eq(i).attr('pgid');
			var pid = $('.tbodyfir tr').eq(i).attr('pid');

			// 默认显示手机类
			if(pid==1|| pgid ==1){
				$('.tbodyfir tr').eq(i).removeClass('hidden')
			}else{
				$('.tbodyfir tr').eq(i).addClass('hidden')
			}
			// 当pid和pgid与当前option的值相同的时候展示分类
			if(parTr == pid || parTr == pgid){
				$('.tbodyfir tr').eq(i).removeClass('hidden')
			}else{
				$('.tbodyfir tr').eq(i).addClass('hidden')
			}
			console.log(parTr,pid,pgid)
		}				
	});
}
/*---------------------------------------------------*/ 