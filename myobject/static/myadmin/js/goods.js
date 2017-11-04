/*good-index 页面--------------------------------------------------*/
//列表中的性别和状态将数字显示为中文
function gStateChange(){
	var trLisr = $('tbody tr');
	var i =0;
	while(i < trLisr.length){
		var stateg = $('tbody tr').eq(i).find('.goodsState').text();
		if(stateg == 3){
			$('tbody tr').eq(i).find('.goodsState').text('下架');
		}else if(stateg == 1){
			$('tbody tr').eq(i).find('.goodsState').text('新添加');
		}else if(stateg == 2){
			$('tbody tr').eq(i).find('.goodsState').text('在售');
		}
		i++;
	}
}

//单价保留两位小数
function blTwoXs(){
	var priceInt = $('.goodsprice input[name=price]').val();
	var priceIntSec = $('.table  .goodsprice').text();
	var priceDec = parseInt(priceInt);
	var priceDecSec = parseInt(priceIntSec);
	priceDec = priceDec.toFixed(2);
	priceDecSec = priceDecSec.toFixed(2);
	$('.goodsprice input[name=price]').val(priceDec);
	$('.table  .goodsprice').text(priceDecSec);
}
/*---------------------------------------------------------------------------*/
/*goods-edit 页面--------------------------------------------------*/

//商品状态默认选中状态
function goodStateState(){
	var stateChoice = $('#goodStateChoice').val();
	if(stateChoice == 1){
		$("#stateAdd").prop("checked", true);
	}else if(stateChoice == 2){
		$('#stateSale').prop("checked", true);
	}else{
		$('#stateDown').prop("checked", true);
	}
}
//option去重
function  goodsCompany(){
	$("#goodsCompany select").each(function(i,n){
	        var options = "";
	        $(n).find("option").each(function(j,m){
	            if(options.indexOf($(m)[0].outerHTML) == -1)
	            {
	                options += $(m)[0].outerHTML;
	            }
	        });
	        $(n).html(options);
	        console.log(n)
	}); 	
}

/*---------------------------------------------------------------------*/

/*goods-add 页面--------------------------------------------------*/

//用户添加正则判断
function addUsersVerify(){
	//   提交
	var typeidOk=false;
	var goodsOk=false;
	var companyOk=false;
	var descrOk=false;
	var picnameOk=false;
	var storeOk=false;
	var priceOk=false;

	//商品类别id丧失焦点事件
	$('input[name=typeid]').blur(function(){
		//获取商品类别id进行正则获取
		var v =$(this).val();
		var reg=/^\w{1,32}$/;
		//判断如果为true则通过
		if(reg.test(v)){
	                	$(this).css('border-color','#52a8ec');
	                	$('#typeidVerify').addClass('hidden');
	                	typeidOk=true;
		}else{
	                	$(this).css('border-color','#d80000');
	                	$('#typeidVerify').removeClass('hidden');
	                	$('#typeidVerify').html("请输入格式商品类别id")
	                	typeidOk=false;
		}
	})
	//商品名称丧失焦点事件
	$('input[name=goods]').blur(function(){
		//获取商品名称进行正则获取
		var v =$(this).val();
		var reg=/^\S{1,16}$/;
		//判断如果为true则通过
		if(reg.test(v)){
	                	$(this).css('border-color','#52a8ec');
	                	$('#goodsVerify').addClass('hidden');
	                	nameOk=true;
		}else{
	                	$(this).css('border-color','#d80000');
	                	$('#goodsVerify').removeClass('hidden');
	                	$('#goodsVerify').html("请输入格式正确的商品名称")
	                	nameOk=false;
		}
	})
	//商品生产厂家丧失焦点事件
	$('input[name=company]').blur(function(){
	            //获取商品生产厂家
	            var v =$(this).val();
	            var reg=/^[\u4E00-\u9FA5\uF900-\uFA2D\s\w]{1,32}$/;
	            //判断如果为true则通过
	            if(reg.test(v)){
			$(this).css('border-color','#52a8ec');
			$('#companyVerify').addClass('hidden');
			passOk=true;
	            }else{
		    	$(this).css('border-color','#d80000');
		    	$('#companyVerify').removeClass('hidden');
		    	$('#companyVerify').html("请输入格式正确的商品生产厂家")
		    	passOk=false;
	            }
	})
	//商品简介丧失焦点事件
	$('input[name=descr]').blur(function(){
	            //获取商品简介
	            var v =$(this).val();
	            var reg=/^[\u4E00-\u9FA5\uF900-\uFA2D\s\w]{0,255}$/;
	            //判断如果为true则通过
	            if(reg.test(v)){
			$(this).css('border-color','#52a8ec');
			$('#descrVerify').addClass('hidden');
			descrOk=true;
	            }else{
		    	$(this).css('border-color','#d80000');
		    	$('#descrVerify').removeClass('hidden');
		    	$('#descrVerify').html("请输入格式正确的商品简介")
		    	descrOk=false;
	            }
	})
	//商品单价丧失焦点事件
	$('input[name=price]').blur(function(){
	            //获取商品单价
	            var v =$(this).val();
	            var reg=/^\d+(\.\d{2})$/;
	            //判断如果为true则通过
	            if(reg.test(v)){
			$(this).css('border-color','#52a8ec');
			$('#priceVerify').addClass('hidden');
			priceOk=true;
	            }else{
		    	$(this).css('border-color','#d80000');
		    	$('#priceVerify').removeClass('hidden');
		    	$('#priceVerify').html("请输入格式正确的商品单价")
		    	priceOk=false;
	            }
	})
	//商品库存量丧失焦点事件
	$('input[name=store]').blur(function(){
	            //获取商品库存量
	            var v =$(this).val();
	            var reg=/^\d+$/;
	            //判断如果为true则通过
	            if(reg.test(v)){
			$(this).css('border-color','#52a8ec');
			$('#storeVerify').addClass('hidden');
			storeOk=true;
	            }else{
		    	$(this).css('border-color','#d80000');
		    	$('#storeVerify').removeClass('hidden');
		    	$('#storeVerify').html("请输入格式正确的商品库存量")
		    	storeOk=false;
	            }
	})
}

/*---------------------------------------------------------------------*/