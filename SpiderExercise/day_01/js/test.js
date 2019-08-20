
var plan = 'Nine Square';
var planColor='#00ff00';
var bgcolor = '#ffffff';
var radicalColor = '#0000ff';
var strokeColor = '#000000';
var transientColor = '#ff0000';
if(transientColor.length == 1)
	transientColor = '';

function getPhraseFor(wc)
{
    document.myform.action = "/common/fcg/estroke.fcg?task=getPhrase";
    if(wc.length != 0)
		document.myform.uni.value= wc;
    document.myform.xx.value=''
    document.myform.submit();
    return false;
}

function pronouncePinyin(oid)
{
    document.myform.action =
		"http://www.eon.com.hk/common/fcg/estroke.fcg?task=getPinyinAudio&pinyin=" + oid.id;
	document.myform.submit();
/*
	var audio = document.getElementById('audio');
	audio.setAttribute('src',
		"http://www.eon.com.hk/common/fcg/estroke.fcg?task=getPinyinAudio&pinyin=" + oid.id);
	audio.play();
*/
	var pdiv = document.getElementById('pinyinsDiv');
	pdiv.style.visibility ='hidden';
}
function setCurrentPinyin(p)
{
	var tbl = document.getElementById('pinyins');
	while(tbl.firstChild)
		tbl.removeChild(tbl.firstChild);
	var pys = p.split(" ");
	for(var i=0; i<pys.length; ++i){
		var row = tbl.insertRow(tbl.rows.length);
		var cell = row.insertCell(0);
		var element = document.createTextNode(pys[i]);
		cell.appendChild(element);
		cell.id = pys[i];
		cell.setAttribute('onClick','pronouncePinyin(this)');
	}
}
function startAnimate(c,s,p)
{
	new PhraseAnimate(c,s,p);
	var pdiv = document.getElementById('pinyinsDiv');
	pdiv.scrollTop = 0;
}

function pronounce()
{
	var pinyins = document.getElementById('pinyins').getElementsByTagName('tr');
	if(pinyins.length == 1)
		pronouncePinyin(pinyins[0].cells[0]);
	else if(pinyins.length > 1) {
		var pdiv = document.getElementById('pinyinsDiv');
		pdiv.style.visibility = 'visible';
	}
}

function submitForm()
{
	var wc = document.myform.xx.value;
	for(var i=0; i<wc.length; ++i){
		if(wc.charAt(i) != ' '){
			document.myform.uni.value = wc.charAt(i);
			document.myform.xx.value='';
			document.myform.submit();
			break;
		}
	}
	return false;
}
function init()
{
	drawPlan('eStroke');
	var canvas = document.getElementById('eStroke');
	var pdiv = document.getElementById('pinyinsDiv');
	pdiv.style.top = canvas.style.top;
	pdiv.style.left = canvas.style.left;
	document.myform.xx.focus();
}