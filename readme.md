# Seal Project 4

- **Name**: Erick Valencia
- **App**: What's in my kitchen cabinet
- **Description**: Application to track your copious amount of dishes in your home. Know what you need and don't need
- **Deployed**: https://project-4-backend-ytqt.onrender.com/

## List of Dependencies

- django-cors-headers
- djangorestframework
- djangorestframework-simplejwt
- pyJWT

### Frontend: React

### As a User
- I want to create an account
- I want to sign into my account
- I want to view all of my collection
- I want to view specific parts of my collection
- I want to create new cups or plates
- I want to remove my cups or plates
- I want to update my cups or plates

#### Route mapping

| Route Name | Endpoint | Method | Description |
|------------|----------|--------|-------------|
| Signup | /singup | GET | create a user |
| Login | /login | GET | sign in |
| Index | /collection | GET | Bring to index page |
| Cup ID Show | /collection/cup/:id | GET | Bring to specific cup ID |
| Plate ID Show | /collection/plate/:id | GET | Bring to a specific plate ID |
| New cup | /collection/cup/new | GET | Bring to creating a new cup |
| New plate | /collection/plate/new | GET | Bring to creating a new plate |
| Create cup | /collection | POST | Create new cup and return to index |
| Create plate | /collection | POST | Create a new plate and return to index |
| Update cup | /collection/cup/:id | PUT | Update an existing cup |
| Update plate | /collection/plate/:id | PUT | Update an existing plate |
| Delete cup | /collection/cup/:id | DELETE | Delete cup and return to index |
| Delete plate | /collection/plate/:id | DELETE | delete a plate and return to index |


## ERD

![ERD](https://i.imgur.com/CABjmmV.jpg)

## Design mockup

![Create User](https://i.imgur.com/xBDMIsP.jpg)
![Login user](https://i.imgur.com/HchKNuo.jpg)
![Index page](https://i.imgur.com/rO5hRsi.jpg)
![Cup :id page](https://i.imgur.com/2kZOF65.jpg)
![Plate :id page](https://i.imgur.com/mnZpwt1.jpg)
![Create Cup](https://i.imgur.com/9oSreil.jpg)
![Create Plate](https://i.imgur.com/zPNKIrn.jpg)
![Update cup](https://i.imgur.com/r3V2GWV.jpg)
![Update plate](https://i.imgur.com/pEBXLfo.jpg)