import React from "react";

const ProfilePage = ({ user }) => {
    return (
        <div>
            <h1>{user.username}'s Profile</h1>
            {user.profile_picture ? (<img src={user.profile_picture} alt="ProfilePic"/>): (<p>No profile picture</p>)}
            <p>Bio: {user.bio}</p>
            <p>Date of Birth: {user.date_of_birth}</p>
        </div>
    );
};

export default ProfilePage;