import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CalendarOptions } from '@fullcalendar/core'; // useful for typechecking
import dayGridPlugin from '@fullcalendar/daygrid';
import bootstrapPlugin from '@fullcalendar/bootstrap';
import interactionPlugin from '@fullcalendar/interaction';
import { FullCalendarModule } from '@fullcalendar/angular';

@Component({
  selector: 'app-time-calendar',
  standalone: true,
  imports: [CommonModule, FullCalendarModule],
  templateUrl: './time-calendar.component.html',
  styleUrls: ['./time-calendar.component.scss']
})
export class TimeCalendarComponent {
  calendarOptions: CalendarOptions = {
    headerToolbar: false,    
    titleFormat: { year: 'numeric', month: 'short' },
    initialView: 'dayGridMonth',
    plugins: [dayGridPlugin, bootstrapPlugin, interactionPlugin],
    expandRows: true,
    contentHeight: 400,
    themeSystem: 'bootstrap',
    selectable: true,
    dayMaxEvents: true, // allow "more" link when too many events
    navLinks: true,     // day headings and weekNumbers will become clickable.
    events: [
      {
        title: "8:10",
        start: new Date(2023,1,3,8,10,0)
      },
      {
        title: "12:00",
        start: new Date(2023,1,3,12,0,0)
      },
      {
        title: "13:00",
        start: new Date(2023,1,3,13,0,0)
      },
      {
        title: "17:10",
        start: new Date(2023,1,3,17,10,0)
      }
    ]
  };
}
