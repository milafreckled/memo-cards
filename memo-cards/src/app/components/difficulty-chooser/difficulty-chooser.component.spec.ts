import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DifficultyChooserComponent } from './difficulty-chooser.component';

describe('DifficultyChooserComponent', () => {
  let component: DifficultyChooserComponent;
  let fixture: ComponentFixture<DifficultyChooserComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DifficultyChooserComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DifficultyChooserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
