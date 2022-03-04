import React, { useState } from "react";

import {Button, Card, Container, Placeholder} from "react-bootstrap";




function CreatePost(prop) {
    const [userID, setUserID] = useState("732ea04f-20ed-431c-90b4-342195bf74c8");
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

    const handleSubmit = async (e) => {
        e.preventDefault();
        let data = {
            title : title,
            visibility: visibility,
            content: content,
            description: description,
            categories: [],
        }
        try {
            await axios.post(`http://127.0.0.1:8000/service/authors/${userID}/posts`, data, config)
            console.log("Success!")
            setOpen(true)
    
           window.history.back("/events")
        } catch (error) {
            console.log(error.message);
            setOpen(true)
        }
      }

    return (
        <Container>
            <Card profile>
                    <CardBody profile>
                    <h1 className={classes.cardTitle}>Create New Event</h1>
                    <h5>Event Holder : {username}</h5>
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
                        Submit
                    </Button>
                    <Button color="primary" round component={Link} to='/home'>
                        Cancel
                    </Button>
                    </CardBody>
                  </Card>
        </Container>
    )
}

export default CreatePost;