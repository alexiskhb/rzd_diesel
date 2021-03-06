document.getElementById('ex2').setAttribute('data-slider-value', "[" + 0 + ", " + (Math.floor(Date.now()) - 60*60*24*365*47*1000) + "]");
document.getElementById('ex2').setAttribute('data-slider-min', 0);
document.getElementById('ex2').setAttribute('data-slider-max', (Math.floor(Date.now()) - 60*60*24*365*47*1000));
document.getElementById('ex2').setAttribute('data-slider-step', 10000);

var slider = new Slider('#ex2', {});

function check_cor(val)
{
	if (val < 10)
		return "0" + String(val);
	return val;	
}

function timeConverter(UNIX_timestamp){
  let a = new Date(UNIX_timestamp * 1000);
  let months = ['Янв','Фев','Мар','Апр','Май','Июн','Июл','Авг','Сен','Окт','Ноя','Дек'];

  let year = a.getFullYear();
  let month = months[a.getMonth()];
  let date = a.getDate();
  let hour = check_cor(a.getHours());
  let min = check_cor(a.getMinutes());
  let sec = check_cor(a.getSeconds());
  let time = date + ' ' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec ;
  return time;
}

start_time  = 0;
end_time = 0;

$('#ex2').on('change', function(e) {
	var data = e.target.value.split(',');
	document.getElementById("start_time").textContent = timeConverter(data[0]/1000);
	start_time = data[0];
	document.getElementById("end_time").textContent = timeConverter(data[1]/1000);
	end_time = data[1];
})
//$('#ex2').data-slider-max 

Math.floor(Date.now() / 1000)