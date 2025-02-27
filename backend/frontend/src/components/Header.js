import React from "react";
import { Link } from "react-router-dom";

const Header = () => {
    return (
        <header>
            <nav>
                <Link to="/">Home</Link>
                <br />
                <Link to="/profile">Profile</Link>
            </nav>
        </header>
    );
};

export default Header;