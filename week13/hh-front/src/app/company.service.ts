import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import {HttpClient} from '@angular/common/http';
import {Company, LoginResponse} from './models';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  BASE_URL = 'http://localhost:8000';

  constructor(private http: HttpClient) {
  }

  getCompanyList(): Observable<Company[]> {
    return this.http.get<Company[]>(`${this.BASE_URL}/api/companies/`);
  }

  getCompany(id): Observable<Company> {
    return this.http.get<Company>(`${this.BASE_URL}/api/companies/${id}/`);
  }

  login(username, password): Observable<LoginResponse> {
    // @ts-ignore
    // @ts-ignore
    return this.http.post(`${this.BASE_URL}/login/`, {
      username,
      password
    });
  }
}
