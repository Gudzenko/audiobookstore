import React from "react";
import { Route, Routes } from "react-router-dom";
import Home from "../screens/Home/Home";
import AudioList from "../screens/AudioList/AudioList";

const MainContent: React.FC = () => {
  return (
    <>
      <Routes>
        <Route path="/hom" element={<Home />} />
        <Route path="/audios" element={<AudioList />} />
      </Routes>
    </>
  );
};

export default MainContent;
