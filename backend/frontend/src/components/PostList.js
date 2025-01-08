import React, { useEffect, useState } from 'react';
import { fetchPosts } from '../services/api';

const PostList = () => {
    const [posts, setPosts] = useState([]);
    const [error, setError] = useState('');

    useEffect(() => {
        // Fetch posts from the API when page loads
        fetchPosts()
            .then((response) => setPosts(response.data))
            .catch((err) => setError('Failed to fetch posts'));
    }, []);

    if (error) {
        return <p>{error}</p>
    }

    return (
        <ul>
            {posts.map(post => (
                <li key={post.id}>
                    <p>{post.user.username} - {post.content}</p>
                </li>
            ))}
        </ul>
    )

};

export default PostList;

