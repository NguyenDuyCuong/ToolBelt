import { AppState } from '@/store/state';
import { UiState } from '@/store/ui/state';
import { Component, OnInit } from '@angular/core';
import { TimeCalendarComponent } from '@components/time-calendar/time-calendar.component';
import { TimeLineComponent } from '@components/time-line/time-line.component';
import { Store } from '@ngrx/store';
import { Observable } from 'rxjs';


@Component({
  selector: 'app-working-time',
  templateUrl: './working-time.component.html',
  styleUrls: ['./working-time.component.scss']
})
export class WorkingTimeComponent implements OnInit {
  public ui: Observable<UiState>;
  public workingTimeCalendar: boolean;
  
  constructor(
      private store: Store<AppState>
      
  ) {}

  ngOnInit(): void {
    this.ui = this.store.select('ui');
    this.ui.subscribe((state: UiState) => {
        this.workingTimeCalendar = state.workingTimeCalendar;
    });
  }
}
