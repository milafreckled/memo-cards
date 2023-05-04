import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpEvent, HttpHandler, HttpHeaders, HttpInterceptor, HttpRequest } from '@angular/common/http'
import { catchError, map, Observable, throwError } from 'rxjs';
export interface ITerm{
  id?: number;
  term: string;
  definition: string
}
interface ITermId{
  termId: number;
}
@Injectable({
  providedIn: 'root'
})

export class DbServiceService implements HttpInterceptor {
  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    console.info(`Http request info: ${request.url}, ${request.method}, ${request.body}`);
    return next.handle(request);
  }
  httpOptions = { 
    headers: new HttpHeaders({'content-type': 'application/json'})
  };
  private handleError(error: HttpErrorResponse){
    if (error.status === 0){
      console.error('An error occured:', error.error)
    }else{
      console.error(`Backend responded with error ${error.status}: ${error.error}`);
    }
    return throwError(() => new Error('Something bad happened. Please try again'))
  }

  constructor(private http: HttpClient) { }
  rootUrl = 'api'
  getTerms(): Observable<ITerm[]>{  
   return this.http.get<ITerm[]>(`/${this.rootUrl}/terms`).pipe(catchError(this.handleError));
  }
  deleteTerm(termToDelete: string){
    return this.http.delete(`/${this.rootUrl}/deleteTerm/${termToDelete}`, this.httpOptions).pipe(catchError(this.handleError));
  }
  addTerm(newTerm: ITerm){
    return this.http.post(`/${this.rootUrl}/addTerm`,  { newTerm },
    this.httpOptions).pipe(catchError(this.handleError));
  };
  getTermId(term: string){
    return this.http.post<{
      fields: any
    }>(`/${this.rootUrl}/getTermId`,  { term },
    this.httpOptions).pipe(catchError(this.handleError));
  };
  getTermBySearch(term: string){
    return this.http.post<{
      fields: any
}>(`/${this.rootUrl}/getTerm`,  { term },
    this.httpOptions).pipe(catchError(this.handleError));
  }
updateTerm(term: ITerm ){
    return this.http.put(`/${this.rootUrl}/updateTerm`, {
      id: term.id,
      term: term.term,
      definition: term.definition 
    },
    this.httpOptions).pipe(catchError(this.handleError));
  }
}
