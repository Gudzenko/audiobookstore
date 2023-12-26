import React from "react";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import { PersistGate } from "redux-persist/integration/react";
import { Provider } from "react-redux";
import Sidebar from "./screens/SideMenu/SideMenu";
import MainContent from "./routes/MainContent";
import Login from "./screens/Login/Login";
import ProtectedRoute from "./routes/ProtectedRoute";
import store, { persistor } from "./store";

const App: React.FC = () => {
  return (
    <Provider store={store}>
      <PersistGate persistor={persistor} loading={null}>
        <Router>
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route
              path="/*"
              element={
                <>
                  <Sidebar />
                  <MainContent />
                </>
              }
            />
          </Routes>
          <ProtectedRoute />
        </Router>
      </PersistGate>
    </Provider>
  );
};

export default App;
