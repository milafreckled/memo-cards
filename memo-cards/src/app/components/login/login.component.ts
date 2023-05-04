import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { AuthService } from 'src/app/services/auth.service';
import { GoogleApiService, UserInfo } from 'src/app/services/google-api.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  userInfo?: UserInfo;
  loginResponse = '';
  loginForm = new FormGroup({
    name: new FormControl('', [Validators.required, Validators.pattern(/[a-zA-Z]/)]),
    email: new FormControl('', [Validators.required, Validators.pattern(/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/g)])
  });
  name = this.loginForm.get('name');
  email = this.loginForm.get('email');
  constructor (private authService: AuthService, private readonly googleApi: GoogleApiService){
    googleApi.userProfileSubject.subscribe(info => {
      this.userInfo = info;
    });
  };
  isLoggedIn(){
    return this.googleApi.isLoggedIn();
  };
  isLoggedInByEmail(){
    return this.googleApi.loggedInByEmail;
  };
  logOut(){
    this.googleApi.signOut();
  };
  onLogin(){
    if (this.loginForm.valid && this.email?.value && this.name?.value){
      this.googleApi.login(this.email.value, this.name.value).subscribe(data => this.loginResponse = JSON.stringify(data))
    }
  }
  onSubmit(){
    this.onLogin();
    // if (this.loginForm.valid && this.name!== null && this.email !== null ){
    //   this.authService.login(this.name, this.email).subscribe(result => console.log(result));
    //   this.authService.setToken();
    // }
  }
}
