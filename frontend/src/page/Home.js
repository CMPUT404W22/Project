import React, {useState, useEffect} from "react";

import {Button, Card, Container, Placeholder} from "react-bootstrap";
import { Link } from 'react-router-dom';
import { Typography, Tooltip, IconButton } from "@material-ui/core";
import EditIcon from '@material-ui/icons/Edit';
import Fab from "@material-ui/core/Fab";
import AddIcon from "@material-ui/icons/Add";
import contentStyles from "./styles/classContent";
import axios from "axios";


function Home(prop) {
    const classesContent = contentStyles();
    const [userID, setUserID] = useState("732ea04f-20ed-431c-90b4-342195bf74c8");
    const [open, setOpen] = useState(false);
    const [cardInfo, setCardInfo] = useState([]);
    const config = {
      headers: {
          'Content-Type': 'application/json'
      }
    };

    useEffect(() => {
      const fetchUser = async () => {
          try {
            axios.get(`http://127.0.0.1:8000/service/authors/${userID}/posts/`, config)
            .then(function (res){
              let _data = res.data.items
              // console.log("read:",_data)
              setCardInfo(_data)
     
             });
             } catch (error) {
                 console.log(error.message);
                 
             }
      }
      fetchUser();
    }, []);

    const handleSubmit = async (card, e) => {
        let lastSegment = card.split("/").pop()
        console.log("id", lastSegment)
        window.location.href = `/post/${lastSegment}`
    }

    const renderCard = (card, index) => {
        return (
            <Card style = {{margin: '30px'}} key = {index}>
              <Tooltip title="Edit or Delete Post" style={{ position: 'absolute', right: 5, top: 5 }}>
                <IconButton onClick={() =>handleSubmit(card.id)}>
                  <EditIcon className={classesContent.block} color="primary"/>
                </IconButton>
              </Tooltip>
              <Card.Body>
                <h3>{card.title}</h3>
                <Card.Text>Author: {card.author.displayName}</Card.Text>
                <Card.Text>Update Date: {new Intl.DateTimeFormat('en-US', {year: 'numeric', month: '2-digit',day: '2-digit', hour: '2-digit', minute: '2-digit'}).format(new Date(card.published))}</Card.Text>
                <Card.Text>Description: {card.description}</Card.Text>
                <Card.Text>Content: {card.content}</Card.Text>
              </Card.Body>
          </Card>
        )
      }

    return (
        <Container>
          <div className={classesContent.contentWrapper}>
              {cardInfo.length > 0 ?
                cardInfo.map(renderCard) :
                <Typography color="textSecondary" align="center">
                  No post Yet
                </Typography>
              }
            </div>
          <Fab size="medium" color="primary" aria-label="add" className={classesContent.fab} component={Link} to='/post/create_post' style={{ color: "white", textDecoration: "none" }}>
            <AddIcon />
          </Fab>
        </Container>
    )
}

export default Home;