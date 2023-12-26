import React from "react";
import { Navigate, useLocation } from "react-router-dom";
import { useSelector } from "react-redux";
import { RootState } from "../store";

const ProtectedRoute: React.FC = () => {
  const LOGIN_URL = "/login";
  const auth = useSelector((state: RootState) => state.auth);
  const location = useLocation();

  return <Navigate to={auth.account ? location.pathname : LOGIN_URL} replace />;
};

export default ProtectedRoute;
