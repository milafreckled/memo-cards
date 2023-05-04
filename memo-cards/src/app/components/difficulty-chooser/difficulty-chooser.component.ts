import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-difficulty-chooser',
  templateUrl: './difficulty-chooser.component.html',
  styleUrls: ['./difficulty-chooser.component.css']
})
export class DifficultyChooserComponent {
  chosenLevelValue: string = "easy";
  @Output()
  changeDifficultyLevel: EventEmitter<string> = new EventEmitter<string>();
  onDifficultyLevelChanged(){
    this.changeDifficultyLevel.emit(this.chosenLevelValue);
  }
}
