import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { };
  httpOptions = { 
    headers: new HttpHeaders({'content-type': 'application/json'})
  };
  login(name: string | null | undefined, email: string | null | undefined){
    return this.http.post('/login', { name, email} , this.httpOptions)
    .pipe(catchError(err => { throw new Error('Error while logging in'+err) }))
  };
  setToken(){
    localStorage.setItem('token', 'S+kX/wwuZOVQAK6A0gE3/2CYs3yMmx49');
  };
  getToken(){
    return localStorage.getItem('token');
  };
  isLoggedIn(){
    return this.getToken() != null;
  }
}
