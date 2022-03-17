// region imports

// react
import React from 'react';
import ReactDOM from 'react-dom';
import {Helmet} from 'react-helmet'
import {BrowserRouter, Route, Routes,} from "react-router-dom";

// component

import TopNavigationBar from "./component/TopNavigationBar/TopNavigationBar";
import DevMenu from "./component/DevMenu/DevMenu";
import Home from "./page/Home";
import About from "./page/About";
import SignIn from "./page/SignIn";
import SignUp from "./page/SignUp";
import NotFound404 from "./page/NotFound404";
import PrivateRoute from "./auth/PrivateRoute";
import UserProfile from "./page/UserProfile";
import CreatePost from './page/CreatePost';
import EditPost from './page/Edit_Delete_post';

// css
import './global.css';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';

// utility
import reportWebVitals from './reportWebVitals';
import Global from "./utility/Global";
import Inbox from "./page/Inbox";



// endregion

// region main render
ReactDOM.render(
    <React.Fragment>
        <Helmet>
            <title>{Global.TITLE}</title>
        </Helmet>

        <TopNavigationBar/>
        <DevMenu/>
        <BrowserRouter>
            <Routes>
                {/* region public pages */}
                <Route exact path="/about" element={<About/>}/>
                <Route exact path="/sign-up" element={<SignUp/>}/>
                <Route exact path="/sign-in" element={<SignIn />} />
                {/* endregion */}

                {/* region user pages, require auth */}
                <Route exact path='/user-profile' element={<PrivateRoute/>}>
                    <Route exact path='/user-profile' element={<UserProfile/>}/>
                </Route>

                <Route exact path='/' element={<PrivateRoute/>}>
                    <Route exact path='/' element={<Home/>}/>
                </Route>

                <Route exact path='/home' element={<PrivateRoute/>}>
                    <Route exact path='/home' element={<Home/>}/>
                </Route>

                <Route exact path='/inbox' element={<PrivateRoute/>}>
                    <Route exact path='/inbox' element={<Inbox/>}/>
                </Route>
                
                <Route exact path='/post/create_post' element={<CreatePost/>}/>
                <Route exact path='/post/:post_id' element={<EditPost/>}/>
                {/* endregion */}

                <Route path="*" element={<NotFound404/>}/>
            </Routes>
        </BrowserRouter>
    </React.Fragment>,
    document.getElementById('root')
);
// endregion

// region web vitals
// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
// endregion
