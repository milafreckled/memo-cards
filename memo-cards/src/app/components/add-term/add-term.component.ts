import { Component, Input, SimpleChanges } from '@angular/core';
import { AbstractControl, AsyncValidator, FormBuilder, FormControl, FormGroup, NgForm, ValidationErrors, Validators } from '@angular/forms';
import { of } from 'rxjs';
import { DbServiceService, ITerm } from '../../services/db-service.service';

@Component({
  selector: 'app-add-term',
  templateUrl: './add-term.component.html',
  styleUrls: ['./add-term.component.css']
})

export class AddTermComponent implements AsyncValidator {
  @Input() editMode = false;
  @Input() editTerm!: ITerm;
  editTermId!: number | null;
  submitted=false;
  newTermForm = new FormGroup({
    term: new FormControl('', [Validators.required, Validators.pattern(/[a-zA-Z]/)]),
    definition: new FormControl('', [Validators.required]),
  });
  
term = this.newTermForm.get('term');
definition = this.newTermForm.get('definition');
constructor(private fb: FormBuilder,private dbService: DbServiceService){};
ngOnInit(){
  if (this.editMode && this.editTerm){
    this.dbService.getTermId(this.editTerm.term).subscribe((res) => {
      const id = res.fields.find((f: { name: string; }) => f.name === "id").columnID;
      this.editTermId = id;
    });
  }
};
validate(control: AbstractControl): Promise<ValidationErrors|null>{
  if (control.dirty || control.touched && control.errors){
    return Promise.resolve({control: 'catched'});
  }
  return Promise.resolve(null);
};

onSubmit(): void{
  this.submitted=true;
  let newTerm: ITerm;
  if (this.term?.value && this.definition?.value){
    newTerm  = {
      term: this.term?.value,
      definition: this.definition?.value
    }
    if (!this.editMode){
      this.dbService.addTerm(newTerm).subscribe((res: any) => console.log('Add result:', res));
    }else{
      if (this.editTermId && this.term && this.definition){
        const termToUpdate: ITerm = {
          id: this.editTermId,
          term: this.term.value,
          definition: this.definition.value
        }
        this.dbService.updateTerm(termToUpdate).subscribe((res: any) => console.log('Update result:', res));
        this.editMode = false;
      }
    }
  }else{
    console.error('No values to submit.')
  }
};

}
