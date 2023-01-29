import { Component, ElementRef, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TimeCardComponent } from "../time-card/time-card.component";

declare const $: any;

@Component({
    selector: 'app-time-line',
    standalone: true,
    templateUrl: './time-line.component.html',
    styleUrls: ['./time-line.component.scss'],
    imports: [CommonModule, TimeCardComponent]
})
export class TimeLineComponent implements OnInit {
  constructor(private el: ElementRef) {}

  ngOnInit(): void {
    
  }

}
