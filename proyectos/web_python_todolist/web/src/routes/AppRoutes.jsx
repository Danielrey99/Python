import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import LoginPage from '../pages/LoginPage';
import RegisterPage from '../pages/RegisterPage';
import ToDoListPage from '../pages/ToDoListPage';
import Layout from '../components/Layout';
import CreateListPage from '../pages/CreateListPage';
import EditListPage from '../pages/EditListPage';
import UserPage from '../pages/UserPage';
import AdminPage from '../pages/AdminPage';
import ListDetailPage from '../pages/ListDetailPage';

function AppRoutes() {
    const isLoggedIn = !!localStorage.getItem('token');
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Navigate replace to={isLoggedIn ? "/todolist" : "/login"} />} />
                <Route path="/login" element={isLoggedIn ? <Navigate replace to="/todolist" /> : <LoginPage />} />
                <Route path="/register" element={isLoggedIn ? <Navigate replace to="/todolist" /> : <RegisterPage />} />
                <Route path="/todolist" element={isLoggedIn ? <Layout><ToDoListPage /></Layout> : <Navigate replace to="/login" />} />
                <Route path="/create-list" element={isLoggedIn ? <Layout><CreateListPage /></Layout> : <Navigate replace to="/login" />} />
                <Route path="/edit-list/:id" element={isLoggedIn ? <Layout><EditListPage /></Layout> : <Navigate replace to="/login" />} />
                <Route path="/user" element={isLoggedIn ? <Layout><UserPage /></Layout> : <Navigate replace to="/login" />} />
                <Route path="/list/:id" element={isLoggedIn ? <Layout><ListDetailPage /></Layout> : <Navigate replace to="/login" />} />
                <Route path="/admin" element={isLoggedIn && localStorage.getItem('rol') === 'admin' ? <Layout><AdminPage /></Layout> : <Navigate replace to="/login" />} />
            </Routes>
        </BrowserRouter>
    );
}

export default AppRoutes;