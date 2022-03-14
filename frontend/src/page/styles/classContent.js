import { makeStyles } from '@material-ui/core/styles';

const contentStyles = makeStyles((theme) => ({
    paper: {
      maxWidth: 936,
      margin: 'auto',
      overflow: 'hidden',
    },
    paperT: {
      maxWidth: 936,
      minHeight: 500,
      margin: 'auto',
      overflow: 'auto',
    },
    searchBar: {
      borderBottom: '1px solid rgba(0, 0, 0, 0.12)',
    },
    searchInput: {
      fontSize: theme.typography.fontSize,
    },
    block: {
      display: 'block',
    },
    addUser: {
      marginRight: theme.spacing(1),
    },
    contentWrapper: {
      margin: '40px 16px',
    },
    fab: {
      position: "fixed",
      bottom: theme.spacing(2),
      right: theme.spacing(2),
    },
    buttons: {
      position: 'relative',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      paddingBottom: '1%'
    }

}));

export default contentStyles
