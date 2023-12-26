import React from "react";
import { Drawer, List, ListItem, ListItemText } from "@mui/material";
import { Link, useLocation } from "react-router-dom";

const urls = ["/login"];

const SideMenu = () => {
  const location = useLocation();
  const isAuth = urls.includes(location.pathname);

  return (
    <>
      {!isAuth && (
        <Drawer variant="permanent">
          <List>
            <ListItem component={Link} to="/">
              <ListItemText primary="Home" />
            </ListItem>
            <ListItem component={Link} to="/audios">
              <ListItemText primary="Audio list" />
            </ListItem>
            <ListItem component={Link} to="/login">
              <ListItemText primary="Exit" />
            </ListItem>
          </List>
        </Drawer>
      )}
    </>
  );
};

export default SideMenu;
