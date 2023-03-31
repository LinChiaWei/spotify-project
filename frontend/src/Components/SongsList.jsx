import Grid from '@mui/system/Unstable_Grid';
import { Card,Paper, CardMedia} from '@mui/material';
import React from 'react';

export const SongsList = (props) => {
    return(
      <div>
        <Grid container spacing={2} >
        {props.data.map((item, index) => ( 
              <Grid key={item[0]} xs={6} md={3} padding={2}>
                <Card sx={{
                  border: '5px solid',
                  borderColor: 'DarkSlateGray',
                  backgroundColor: 'black',
                  padding:'0px 5px 2px 5px'
                }}>
                  <Paper sx={{
                    textAlign:'center',
                    fontSize: 25,
                    letterSpacing: 0.5,
                    fontWeight: 'bold',
                    opacity: 0.9,
                    color:'Crimson',
                    backgroundColor: 'black',
                    boxShadow: 1,
                    padding:'2px',
                    borderRadius:2}}
                    justifyContent="center"
                    >
                    <div>
                      Rank {index+1}
                    </div>
                  </Paper>

                  <CardMedia
                  component="img"
                  height="200"
                  image={item[1]}
                  alt={"alt"}
                  sx={{ padding: "0px 0px 0px 0px ", objectFit: "contain"}}
                  />

                  <Paper sx={{
                    fontSize: 15,
                    textAlign:'center',
                    alignItems:'center',
                    fontWeight: 'Medium',
                    color:'white',
                    backgroundColor: 'black',
                    boxShadow: 1,
                    padding:'7px',
                    borderRadius:2
                  }} 
                  justifyContent="center"
                  >
                    <div>
                      {item[0]}
                    </div>
                  </Paper>

                  <Paper sx={{
                    fontSize: 12,
                    textAlign:'center',
                    alignItems:'center',
                    fontWeight: 'Medium',
                    color:'white',
                    opacity: 0.7,
                    backgroundColor: 'black',
                    boxShadow: 1,
                    padding:'3px',
                  }} 
                  justifyContent="center"
                  >
                    <div>
                      Song Count : {item[2]}
                    </div>
                  </Paper>
      
                </Card>
              </Grid>
          ))}
        </Grid>
      </div> 
    )
}