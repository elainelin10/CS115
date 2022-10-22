function ajaxGetRequest(path, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("GET", path);
    request.send();
}

function ajaxPostRequest(path, data, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState===4&&this.status ===200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}

function requestScatter(){
  ajaxGetRequest("/towsByDay",showScatter);
}
function showScatter(response) {
    let towsByDay = JSON.parse(response);
    let towsByDayElem=document.getElementById("SP");
    let text=towsByDayElem.innerHTML;
    towsByDayElem.innerHTML=towsByDay
    var trace={
      x:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
      y:towsByDay
      mode:"markers",
      type:"scatter"
    };
    var data=[trace];
    var layout={
      xaxis:{
        range:[0,32]
        title:{
          text:"Day of the Month"},
      },
      yaxis:{
        range:[0:2000]
        title:{
          text:"#Tows"
        },
      },
      title:"Tows by Day of the Month"
    }
    Plotly.newPlot("SP",data,layout);
}

function requestPie(){
  ajaxGetRequest("/towsByDistrict",showPie);
}
function showPie(response) {
    let data = JSON.parse(response);
    Plotly.newPlot("pie",data,layout);
}

function requestLine(){
  ajaxGetRequest("/towsByMonth",showLine);
}
function showLine(response) {
    let towsByMonth = JSON.parse(response);
    var trace1={
      x:[Jan,Feb,Mar,April,May,June,Jul,Aug,Sep,Oct,Nov,Dec],
      y:towsByMonth

    };
    Plotly.newPlot("line",data,layout);
}