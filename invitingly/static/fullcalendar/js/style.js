document.addEventListener('DOMContentLoaded',function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',

//        以下是我自己加入的套件零件
        locale: 'zh-tw',
        height: 700,
        width: 700,
        navlink: true,
        headerToolbar: {
            left: 'prev,next,today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay', //月:週:天
        },



    });
    calendar.render();
});
