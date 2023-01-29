import { AfterViewChecked, ChangeDetectionStrategy, Component, ElementRef, NgZone, OnInit, Renderer2, ViewChild, ViewContainerRef } from '@angular/core';
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
export class TimeCardComponent implements OnInit, AfterViewChecked {
  @ViewChild('template', { static: true }) template;
  
  constructor(private el: ElementRef, private renderer: Renderer2, private ngZone: NgZone, private viewContainerRef: ViewContainerRef) {}

  ngAfterViewChecked(): void {
    this.ngZone.runOutsideAngular(() => {
      const contentId = Math.random().toString(36).substr(2, 9);
      // this.renderer.setProperty(this.el.nativeElement.nextElementSibling, 'id', contentId);

      var custom_values = [0, 10, 100, 1000, 10000, 100000, 1000000];
      var my_from = custom_values.indexOf(10);
      var my_to = custom_values.indexOf(10000);

      $(this.template).find('.js-range-slider').ionRangeSlider({
        type:"double",
        from_fixed: "true",
        to_fixed:"true",
        grid: true,
        from: my_from,
        to: my_to,
        values: custom_values
    });
    });
  }

  ngOnInit(): void {
    let a = this.viewContainerRef.createEmbeddedView(this.template);
  }
}
