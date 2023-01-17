import { Component, OnInit  } from '@angular/core';
declare const $: any;

@Component({
  selector: 'app-working-time',
  templateUrl: './working-time.component.html',
  styleUrls: ['./working-time.component.scss']
})
export class WorkingTimeComponent implements OnInit  {
  ngOnInit(): void {
    $(".js-range-slider").ionRangeSlider();
  }
}
