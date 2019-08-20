var speed=10;
function getPhraseFor(wc)
{
    document.myform.action = "/common/fcg/estroke1.fcg?task=getPhrase";
    if(wc.length != 0)
		document.myform.uni.value= wc;
    document.myform.xx.value=''
    document.myform.submit();
    return false;
}
function setLineDash(ctx,param)
{
	if(!ctx.setLineDash){
		ctx.setLineDash = function(){};
	}
	ctx.setLineDash(param);
}
