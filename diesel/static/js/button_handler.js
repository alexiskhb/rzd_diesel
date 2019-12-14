var tolerances_min = {
  x: [350, 350, 386, 421, 457, 493, 528, 564, 600, 636, 671, 707, 743, 778, 814, 850],
  y: [0, 60, 100, 180, 262, 407, 527, 660, 790, 945, 1095, 1250, 1405, 1560, 1707, 1850],
  mode: 'lines+markers'
};

var tolerances_max = {
  x: [350, 350, 386, 421, 457, 493, 528, 564, 600, 636, 671, 707, 743, 778, 814, 850],
  y: [0, 70, 120, 198, 300, 445, 575, 720, 860, 1038, 1190, 1370, 1524, 1682, 1791, 1880],
  mode: 'lines+markers'
};

function show_plot(data, textStatus, XHR)
{
  obj_output = JSON.parse(data)
  let oox0 = [], ooy0 = [];
  let oox1 = [], ooy1 = [];
  for (let oo of obj_output.points) {
    if (oo.p == 0 || oo.x < 350) {
      continue;
    }
    if (oo.p % 2 == 0) {
      oox0.push(oo.x);
      ooy0.push(oo.y);
    } else {
      oox1.push(oo.x);
      ooy1.push(oo.y);
    }
  }
  var trace0 = {
    x: oox0,
    y: ooy0,
    mode: 'markers',
    marker: { size: 5 }
  };
  var trace1 = {
    x: oox1,
    y: ooy1,
    mode: 'markers',
    marker: { size: 5 }
  };
  var data = [trace0, trace1, tolerances_min, tolerances_max];
  var layout = {};
  Plotly.newPlot('myDiv', data, layout, {showSendToCloud: true});
}


document.getElementById("requestSumm").onclick = function(e)
{
   // console.log($('#ex2').getvalue.split(','));
   // let pair = $('#ex2').value.split(',')
   // let pair = JSON.parse(document.getElementById('ex2').getAttribute('data-slider-value'));
   // console.log(pair)
//   let pair = [$('#ex2').slider("values")[0], $('#ex2').slider("values")[1]];
    console.log(start_time)
    console.log(end_time)
	$.get("/barabulikanumberone", {
	  train: activeId, 
	  from_time: start_time,
	  to_time: end_time,
	},show_plot)
}

train_mark = -1;

document.getElementById("buttonSend").onclick = function(e)
{
  if (train_mark == -1)
    return;
  $.post("/takeData", JSON.stringify({
    train: activeId,
    from_time: document.getElementById('ex2').getAttribute('data-slider-value').split(',')[0],
    to_time: document.getElementById('ex2').getAttribute('data-slider-value').split(',')[1],
    mark: train_mark
  }))
  console.log(train_mark);
}

document.getElementById("buttonNorm").onclick = function(e)
{
  train_mark = 1;
}

document.getElementById("buttonOkay").onclick = function(e)
{
  train_mark = 2;
}

document.getElementById("buttonBad").onclick = function(e)
{
  train_mark = 3;
}