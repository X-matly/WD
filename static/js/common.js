
$(document).ready(function(){
    $(".but,.upwards").hover( //按钮
        function(){
            $(this).css("background-color", "rgba(195,207,231,0.72)");
        },
        function(){
            $(this).css("background-color", "#c3cfe7");
        }
    )
    $("#input_headlines,#input_ID").focus(function(){ //输入框
        $(this).css("background-color","rgba(45,45,63,0.43)");
    });
    $("#input_headlines,#input_ID").blur(function(){
        $(this).css("background-color","#2D2D3F");
    });
    $("#create_new_note").click(function(){ //页面
        $("#displayall").fadeOut(50);
        $("#code").fadeIn(500);
        getHeight("code");

        var d = new Date();
        var a = d.getFullYear() + "-";
        if (d.getMonth() + 1 >= 10 ){
            var c = (d.getMonth() + 1) + "-";
        }
        else{
            var c = "0" + (d.getMonth() + 1) + '-';
        }
        if (d.getDate() >= 10 ){
            var n = d.getDate();
        }
        else{
            var n = "0" + d.getDate();
        }
        $("#startTime").attr("value",a+c+n);
        $("#startTime").attr("min",a+c+n);
    });

    $("#display_all_note").click(function(){
        $("#code").fadeOut(50);
        $("#displayall").fadeIn(500);
        getHeight("displayall");
    });

    $("#endTime").click(function(){
        $("#endTime").attr("min",$("#startTime").val());
    });
});

//以下是ajax与后端交互
function print_table(data) {
            //朴实的print数据表函数
            var tb = $("<table></table>");
            for (var i = 0; i <= data.length; i++) {
                if (!i) {
                    var head = $("<tr></tr>");
                    for (var k in data[0]) {
                        if (k == "note") continue;
                        var th = "<th>" + k + "</th>";
                        head.append(th);
                    }
                    i++;
                    tb.append(head);
                }
                var event = data[i - 1];
                var tr = $("<tr></tr>");
                for (var j in event) {
                    if (j == "note") continue;
                    if (j == "complete"){
                        if(event[j]){
                            tr.append("<td>已完成</td>");
                        } else{
                            tr.append("<td>未完成</td>");
                        }
                    } else{
                        var td = "<td>" + event[j] + "</td>";
                        tr.append(td);
                    }
                }
                tb.append(tr);
            }
            $("#cue").html(tb);
        }

$.ajax({
    type: "GET",
    url: "tempdata.json", //后端请求地址
    dataType: "json",
    success: function (data) {
        print_table(data);
        //排序
        $(document).ready(function(){
            $("#sort_by_start_date").click(function(){
                data.sort(function(note1, note2) {
                    return Date.parse(parseDate(note1.start_time)) - Date.parse(parseDate(note2.start_time));
                })
                print_table(data);
            });
            $("#sort_by_end_date").click(function(){
                data.sort(function(note1, note2) {
                    return Date.parse(parseDate(note1.end_time)) - Date.parse(parseDate(note2.end_time));
                })
                print_table(data);
            });
            $("#sort_by_significance").click(function(){
                data.sort(function(note1, note2) {
                    return note1.significance - note2.significance;
                })
                print_table(data);
            });
        });
    },
    error: function () {
        alert("Failed");
    }
});

function parseDate(str){ // 把字符串转换为日期格式
    return new Date(Date.parse(str.replace(/-/g,"/")));
}

function getHeight(name) {
    var he=document.getElementById('button_place').offsetHeight;
    var ht=document.getElementById(name).offsetHeight;
	if (he>ht){
        document.getElementById('button_place').style.height=1130 + "px";
	}
	else{
        var div = document.getElementById(name);
		document.getElementById('button_place').style.height=(div.offsetHeight+50) + "px";
	}
}
