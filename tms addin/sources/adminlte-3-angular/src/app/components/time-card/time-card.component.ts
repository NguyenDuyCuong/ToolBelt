import { ChangeDetectionStrategy, Component, ElementRef, NgZone, OnInit, Renderer2 } from '@angular/core';
import { CommonModule } from '@angular/common';

declare const $: any;

@Component({
  selector: 'app-time-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './time-card.component.html',
  styleUrls: ['./time-card.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class TimeCardComponent implements OnInit {
  constructor(private el: ElementRef, private renderer: Renderer2, private ngZone: NgZone) {}

  ngOnInit(): void {
    this.ngZone.runOutsideAngular(() => {
      $(this.el.nativeElement).find('.js-range-slider').ionRangeSlider();
    });
  }

}
