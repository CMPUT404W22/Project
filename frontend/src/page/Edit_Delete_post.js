import React, { useState, useEffect } from "react";

import {Button, Card, Container, Placeholder} from "react-bootstrap";
import { useLocation } from 'react-router-dom'
import axios from "axios";
import CardBody from "./styles/cardBody";
import GridContainer from "./styles/GridContainer";
import GridItem from "./styles/GridItem";
import CustomInput from "./styles/costumInput";
import Identity from "../model/Identity";


let identity = Identity.GetIdentity();
function EditPost(props) {
    const location = useLocation();
    const [username, setUsername] = useState(identity.username);
    const [userID, setUserID] = useState("732ea04f-20ed-431c-90b4-342195bf74c8");
    const [postID, setPostID] = useState("")
    const [open, setOpen] = useState(false);
    const [title, setTitle] = useState("")
    const [visibility, setVisibility] = useState(0)
    const [content, setContent] = useState("")
    const [description, setDescription] = useState("")

    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const auth = {
        auth: {
            username: identity.username,
            password: identity.password
          }

    }

    useEffect(() => {
        const fetchUser = async () => {
            try {
                let pathName = location.pathname;
                let post_id = pathName.split("/").pop();
                await axios.get(`http://127.0.0.1:8000/service/authors/${userID}/posts/${post_id}`, config, auth)
               .then(function (response){
                   let _data = response.data
                   setPostID(post_id)
                //    console.log("read:",postID)
                   setTitle(_data.title)
                   setContent(_data.content)
                   setDescription(_data.description)
       
               });
               } catch (error) {
                   console.log(error.message);
                   setOpen(true)
               }
        }
        fetchUser();
      }, []);
    

    const handleSubmit = async (e) => {
        e.preventDefault();
        let data = {
            title : title,
            visibility: visibility,
            content: content,
            description: description,
            categories: [],
            unlisted: false
        }
        try {
            console.log("start")
            console.log("data", data)
            await axios.post(`http://127.0.0.1:8000/service/authors/${userID}/posts/${postID}`, data, auth, config)
            console.log("Success!")
            setOpen(true)
    
            window.location.href = `/home`
        } catch (error) {
            console.log(error.message);
            setOpen(true)
        }
    }

    const handleCancle = async (e) => {
        window.history.back("/home")
    }

    const handleDelete = async (e) => {
        try {
            console.log("start")
            await axios.delete(`http://127.0.0.1:8000/service/authors/${userID}/posts/${postID}`, config)
            console.log("Success!")
            setOpen(true)
    
           window.history.back("/home")
        } catch (error) {
            console.log(error.message);
            setOpen(true)
        }
    }

    return (
        <Container>
            <Card profile>
                    <CardBody profile>
                    <h1>Edit New Post</h1>
                    <h5>Post Holder : {username}</h5>
                    <GridContainer>
                      <GridItem xs={12} sm={12} md={6}>
                        <CustomInput
                          labelText="Post Title"
                          id="postTitle"
                          formControlProps={{
                              fullWidth: true
                          }}
                          inputProps={{
                              "data-testid": "test-title",
                              value: title,
                              onChange: (e) => setTitle(e.target.value)
                          }}
                        />
                        </GridItem>
                        <GridItem xs={12} sm={12} md={6}>
                        <CustomInput
                            labelText="Description"
                            id="description"
                            inputProps={{
                                "data-testid": "test-des",
                                value: description,
                                onChange: (e) => setDescription(e.target.value)
                            }}
                            formControlProps={{
                                fullWidth: true
                            }}
                        />
                        </GridItem>
                        <GridItem xs={12} sm={12} md={12}>
                        <CustomInput
                          labelText="Post Content"
                          id="content"
                          multiline
                          rows={4}
                          inputProps={{ 
                              "data-testid": "test-contennt",
                              value: content,
                              onChange: (e) => setContent(e.target.value),
                              multiline: true,
                              rows: 5,
                              variant: 'outlined'
                          }}
                          formControlProps={{
                              fullWidth: true,
                              variant: 'outlined'
                          }}
                      />
                      </GridItem>
                    </GridContainer>
                    <Button color="primary" round onClick={handleSubmit} >
                        Updated
                    </Button>
                    <Button color="primary" round onClick={handleCancle}>
                        Cancel
                    </Button>
                    <Button color="primary" round onClick={handleDelete}>
                        Delete
                    </Button>
                    </CardBody>
                  </Card>
        </Container>
    )
}

export default EditPost;