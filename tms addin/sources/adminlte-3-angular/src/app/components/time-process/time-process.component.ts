import { ChangeDetectionStrategy, Component, ElementRef, NgZone, OnInit, Renderer2 } from '@angular/core';
import { CommonModule } from '@angular/common';

declare const $: any;

@Component({
  selector: 'app-time-process',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './time-process.component.html',
  styleUrls: ['./time-process.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class TimeProcessComponent implements OnInit {
  constructor(private el: ElementRef, private renderer: Renderer2, private ngZone: NgZone) { }

  ngOnInit() {
    this.ngZone.runOutsideAngular(() => {
      const contentId = Math.random().toString(36).substr(2, 9);
      this.renderer.setProperty(this.el.nativeElement.children[0], 'id', contentId);

      const checkIn = new Date(2023, 1, 3, 9, 10, 0);
      const checkOut = new Date(2023, 1, 3, 17, 10, 0);

      $(`#${contentId}`).ionRangeSlider({
        type: "double",
        from_fixed: "true",
        to_fixed: "true",
        grid: true,
        from: this.timeToTS(checkIn),
        to: this.timeToTS(checkOut),
        min: this.timeToTS(new Date(2023, 1, 3, 7, 0, 0)),
        max: this.timeToTS(new Date(2023, 1, 3, 18, 0, 0)),
        prettify: this.tsToTime
      });
    });
  }

  timeToTS (datetime: Date) {
    return datetime.valueOf();
  }

  tsToTime(ts) {
    var d = new Date(ts);
    var lang = "en-US";

    return d.toLocaleTimeString(lang, { hour: "2-digit", minute: "2-digit" });
  }
}
