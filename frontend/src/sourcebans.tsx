import React, { useMemo, useState, useEffect, ChangeEvent } from "react";
import { render } from "react-dom";
import { useTable, usePagination, useSortBy } from "react-table";
import axios, { AxiosResponse, AxiosError } from "axios";
import { ProgressBar, Modal, Button } from "react-bootstrap";
import { createStyles, makeStyles, Theme } from "@material-ui/core/styles";
import {
  Paper,
  Table,
  LinearProgress,
  TableBody,
  TableCell,
  TableHead,
  Toolbar,
  Tooltip,
  IconButton,
  TableSortLabel,
  TextField,
  Select,
  TableContainer,
  TableRow,
  TableFooter,
  TablePagination,
  Collapse,
  Box,
  Snackbar,
  Typography,
} from "@material-ui/core";
import { Alert } from "@material-ui/lab";
import { KeyboardArrowUp, KeyboardArrowDown, Search } from "@material-ui/icons";
var dayjs = require("dayjs");
var customParseFormat = require("dayjs/plugin/customParseFormat");

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

const useRowStyles = makeStyles({
  root: {
    "& > *": {
      borderBottom: "unset",
    },
  },
});

const useStylesTable = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      width: "100%",
    },
    paper: {
      width: "100%",
      marginBottom: theme.spacing(2),
    },
    table: {
      minWidth: 750,
    },
    visuallyHidden: {
      border: 0,
      clip: "rect(0 0 0 0)",
      height: 1,
      margin: -1,
      overflow: "hidden",
      padding: 0,
      position: "absolute",
      top: 20,
      width: 1,
    },
  })
);

function App(props): JSX.Element {
  const [orderBy, setOrderBy] = useState("created");
  const [order, setOrder] = useState("-");
  const [page, setPage] = useState(0);
  const [progress, setProgress] = useState(false);
  const columns = useMemo(
    () => [
      {
        Header: "Player",
        accessor: "name",
        sortAccessor: "name",
      },
      {
        Header: "Date",
        accessor: "date_start",
        sortAccessor: "created",
      },
      {
        Header: "Admin",
        accessor: "admin_name",
        disableSortBy: true,
      },
      {
        Header: "Length",
        accessor: "duration",
        disableSortBy: true,
      },
      {
        Header: "Remaining Progress",
        accessor: "progressBar",
        disableSortBy: true,
      },
    ],
    []
  );
  const [bans, setBans] = useState([]);
  const [count, setCount] = useState(0);
  const { getTableProps, getTableBodyProps, headerGroups, prepareRow, rows } =
    useTable(
      {
        columns,
        data: bans,
        initialState: { pageIndex: 1 },
        manualSortBy: true,
      },
      useSortBy,
      usePagination
    );
  const [rowsPerPage, setRowsPerPage] = useState(10);
  const [search, setSearch] = useState(defaultSearch);
  const classes = useStylesTable();

  const getBans = async () => {
    setProgress(true);
    await axios
      .get(
        `/api/bans/?ordering=${order}${orderBy}&page=${
          page + 1
        }&limit=${rowsPerPage}&search=${search}`
      )
      .then((res) => {
        setCount(res.data.count);
        for (let i = 0; i < res.data.results.length; i++) {
          let htmlString = res.data.results[i].duration;
          res.data.results[i].duration = (
            <div dangerouslySetInnerHTML={{ __html: htmlString }}></div>
          );
          let percent = res.data.results[i].percent.percent;
          let progress_bar_class =
            res.data.results[i].percent.progress_bar_class;
          res.data.results[i].progressBar = (
            <ProgressBar animated now={percent} variant={progress_bar_class} />
          );
        }
        setBans(res.data.results);
        setProgress(false);
      })
      .catch((err) => {
        setBans([]);
        setProgress(false);
      });
  };

  useEffect(() => {
    if (!progress) {
      getBans();
    }
  }, [page, orderBy, order, rowsPerPage, search]);

  const handleChangePage = (event, newPage: number) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event: ChangeEvent<HTMLInputElement>) => {
    setRowsPerPage(parseInt(event.target.value, 10));
  };

  return (
    <>
      <TableContainer component={Paper}>
        <EnhancedTableToolbar search={search} setSearch={setSearch} />
        <Table>
          <TableHead>
            {headerGroups.map((headerGroup) => (
              <TableRow {...headerGroup.getHeaderGroupProps()}>
                <TableCell />
                {headerGroup.headers.map((column) => (
                  <TableCell {...column.getHeaderProps()}>
                    <TableSortLabel
                      active={orderBy === column.sortAccessor}
                      direction={order === "" ? "asc" : "desc"}
                      onClick={() => {
                        column.toggleSortBy(!column.isSortedDesc);
                        setOrder(column.isSortedDesc ? "" : "-");
                        setOrderBy(column.sortAccessor);
                      }}
                    >
                      {column.render("Header")}
                      {orderBy === column.id ? (
                        <span className={classes.visuallyHidden}>
                          {order === "-"
                            ? "sorted descending"
                            : "sorted ascending"}
                        </span>
                      ) : null}
                    </TableSortLabel>
                  </TableCell>
                ))}
              </TableRow>
            ))}
            <TableLoader progress={progress} headerGroups={headerGroups} />
          </TableHead>
          <TableBody>
            {rows.map((row) => (
              <Row
                key={row.id}
                row={row.original}
                getBans={getBans}
                setSearch={setSearch}
              />
            ))}
          </TableBody>
          <TableFooter>
            <TableRow>
              <TablePagination
                count={count}
                rowsPerPage={rowsPerPage}
                page={page}
                SelectProps={{
                  inputProps: { "aria-label": "rows per page" },
                  native: true,
                }}
                rowsPerPageOptions={[10, 25, 50, 100]}
                onChangePage={handleChangePage}
                onChangeRowsPerPage={handleChangeRowsPerPage}
              />
            </TableRow>
          </TableFooter>
        </Table>
      </TableContainer>
    </>
  );
}

function TableLoader(props) {
  if (props.progress) {
    return (
      <TableRow>
        <TableCell colSpan={props.headerGroups[0].headers.length}>
          <LinearProgress />
        </TableCell>
      </TableRow>
    );
  }
  return null;
}

const EnhancedTableToolbar = (props) => {
  return (
    <Toolbar>
      <Tooltip title="Filter list">
        <IconButton aria-label="filter list">
          <form
            onSubmit={(event) => {
              event.preventDefault();
              props.setSearch(event.target.search.value);
            }}
          >
            <TextField
              label="Search"
              variant="outlined"
              size="small"
              name="search"
              onChange={(event) => {
                let value = event.target.value;
                if (value === "" || typeof value == "undefined") {
                  props.setSearch("");
                }
              }}
            />
            {"  "}
            <Button type="submit" name="submit" variant="secondary">
              <Search />
            </Button>
          </form>
        </IconButton>
      </Tooltip>
    </Toolbar>
  );
};

function Row(props) {
  const { row, getBans, setSearch } = props;
  const [open, setOpen] = React.useState(false);
  const classes = useRowStyles();
  const [showDelete, setShowDelete] = useState(false);

  const handleCloseDelete = () => setShowDelete(false);
  const handleShowDelete = () => setShowDelete(true);

  const [showUnban, setShowUnban] = useState(false);

  const handleCloseUnban = () => setShowUnban(false);
  const handleShowUnban = () => setShowUnban(true);

  const [showEdit, setShowEdit] = useState(false);

  const handleCloseEdit = () => setShowEdit(false);
  const handleShowEdit = () => setShowEdit(true);

  const [editDetailsData, setEditDetailsData] = useState({});
  const [customReason, setCustomReason] = useState(false);

  const [alertMessage, setAlertMessage] = useState({
    message: "",
    severity: "",
  });

  const generatePreviousBans = () => {
    if (row.totalBans <= 1) {
      return "No previous ban";
    } else {
      return (
        <div>
          {row.totalBans}{"  "}
          <a href='javascript:void(0)' onClick={() => setSearch(row.authid)}>(Search)</a>
        </div>
      );
    }
  }

  const details = [
    {
      accessor: "Steam ID",
      data: (
        <a href={`http://steamcommunity.com/profiles/${row.steam64}/`}>
          {row.authid}
        </a>
      ),
    },
    {
      accessor: "Steam3 ID",
      data: (
        <a href={`http://steamcommunity.com/profiles/${row.steam64}/`}>
          {row.steam3}
        </a>
      ),
    },
    {
      accessor: "Steam Community",
      data: (
        <a href={`http://steamcommunity.com/profiles/${row.steam64}/`}>
          {row.steam64}
        </a>
      ),
    },
    {
      accessor: "Created on",
      data: row.date_start,
    },
    {
      accessor: "Ban length",
      data: row.ban_length,
    },
    {
      accessor: "Ends on",
      data: row.date_end,
    },
    {
      accessor: "Reason",
      data: row.reason,
    },
    {
      accessor: "Banned by Admin",
      data: row.admin_name,
    },
    {
      accessor: "Banned from",
      data: row.sid,
    },
    {
      accessor: "Total Bans",
      data: (
        <div>
          {generatePreviousBans()}
        </div>
      ),
    },
    {
      accessor: `Blocked(${row.blocked.length})`,
      data: row.blocked.join(', ').replace(/\, $/, "")
    },
    {
      accessor: "Link",
      data: (
        <Button
          variant="secondary"
          size="sm"
          onClick={() => {
            navigator.clipboard.writeText(
              `https://tensor.fr/bans/${row.authid}`
            );
            setAlertMessage({
              message: `Link copied to clipboard`,
              severity: "success",
            });
          }}
        >
          Copy to clipboard
        </Button>
      ),
    },
  ];

  const tdStyleDescription: React.CSSProperties = {
    paddingRight: "3rem",
    paddingLeft: "1rem",
    verticalAlign: "top",
    textAlign: "left",
  };

  const tdStyleField: React.CSSProperties = {
    paddingRight: "1rem",
    verticalAlign: "top",
    textAlign: "right",
  };

  const fieldStyle: React.CSSProperties = {
    marginBottom: "1rem",
  };

  const buttonsStyle: React.CSSProperties = {
    textAlign: "right",
  };

  return (
    <>
      <React.Fragment>
        <TableRow className={classes.root} key={row.bid}>
          <TableCell>
            <IconButton
              aria-label="expand row"
              size="small"
              onClick={() => setOpen(!open)}
            >
              {open ? <KeyboardArrowUp /> : <KeyboardArrowDown />}
            </IconButton>
          </TableCell>
          <TableCell align="left">{row.name}</TableCell>
          <TableCell align="left">{row.date_start}</TableCell>
          <TableCell align="left">{row.admin_name}</TableCell>
          <TableCell align="center">{row.duration}</TableCell>
          <TableCell align="center">{row.progressBar}</TableCell>
        </TableRow>
        <TableRow>
          <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
            <Collapse in={open} timeout="auto" unmountOnExit>
              <Box margin={1}>
                <Typography variant="h6" gutterBottom component="div">
                  Ban details
                </Typography>
                <Table size="small" aria-label="purchases">
                  <TableBody>
                    {details.map((detail, i) => {
                      if (i != 0) {
                        return (
                          <TableRow>
                            <TableCell align="left">
                              {detail.accessor}
                            </TableCell>
                            <TableCell align="left">{detail.data}</TableCell>
                          </TableRow>
                        );
                      }
                      return (
                        <TableRow>
                          <TableCell align="left">{detail.accessor}</TableCell>
                          <TableCell align="left">{detail.data}</TableCell>
                          <TableCell rowSpan={11}>
                            {!!is_admin && (
                              <ul>
                                <li>
                                  <a
                                    href='javascript:void(0)'
                                    onClick={() => {
                                      handleShowEdit();
                                    }}
                                  >
                                    Edit Details
                                  </a>
                                </li>
                                <li>
                                  <a
                                    href='javascript:void(0)'
                                    onClick={() => {
                                      handleShowUnban();
                                    }}
                                  >
                                    Unban
                                  </a>
                                </li>
                                <li>
                                  <a
                                    href='javascript:void(0)'
                                    onClick={() => {
                                      handleShowDelete();
                                    }}
                                  >
                                    Delete ban
                                  </a>
                                </li>
                              </ul>
                            )}
                          </TableCell>
                        </TableRow>
                      );
                    })}
                  </TableBody>
                </Table>
              </Box>
            </Collapse>
          </TableCell>
        </TableRow>
      </React.Fragment>
      <Snackbar
        open={alertMessage.message != ""}
        autoHideDuration={6000}
        onClose={() => setAlertMessage({ ...alertMessage, message: "" })}
        anchorOrigin={{ vertical: "bottom", horizontal: "right" }}
      >
        <Alert
          onClose={() => setAlertMessage({ ...alertMessage, message: "" })}
          severity={alertMessage.severity}
          variant="filled"
        >
          {alertMessage.message}
        </Alert>
      </Snackbar>
      <Modal show={showDelete} onHide={handleCloseDelete}>
        <Modal.Header closeButton>
          <Modal.Title>Confirmation</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <p>Are you sure you want to delete this ban?</p>
        </Modal.Body>
        <Modal.Footer>
          <Button
            variant="success"
            onClick={() => {
              axios
                .delete(`/api/bans/${row.bid}`, {
                  headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json",
                  },
                })
                .then(() => {
                  setAlertMessage({
                    message: `${row.name}'s ban was deleted`,
                    severity: "success",
                  });
                  getBans();
                })
                .catch((reason: AxiosError) => {
                  if (reason.response!.status === 403) {
                    setAlertMessage({
                      message: `Permission denied`,
                      severity: "error",
                    });
                  } else {
                    setAlertMessage({
                      message: `An error has occured`,
                      severity: "error",
                    });
                  }
                  console.log(reason);
                })
                .finally(() => handleCloseDelete());
            }}
          >
            Delete Ban
          </Button>
          <Button variant="danger" onClick={handleCloseDelete}>
            Cancel
          </Button>
        </Modal.Footer>
      </Modal>

      <Modal show={showUnban} onHide={handleCloseUnban}>
        <Modal.Header closeButton>
          <Modal.Title>Confirmation</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <p>Are you sure you want to unban this player?</p>
        </Modal.Body>
        <Modal.Footer>
          <Button
            variant="success"
            onClick={() => {
              axios
                .put(
                  `/api/bans/${row.bid}/`,
                  { update_type: 1 },
                  {
                    headers: {
                      "Content-Type": "application/json",
                    },
                  }
                )
                .then(() => {
                  setAlertMessage({
                    message: `${row.name} was unbanned`,
                    severity: "success",
                  });
                  getBans();
                })
                .catch((reason: AxiosError) => {
                  if (reason.response!.status === 403) {
                    setAlertMessage({
                      message: `Permission denied`,
                      severity: "error",
                    });
                  } else {
                    setAlertMessage({
                      message: `An error has occured`,
                      severity: "error",
                    });
                  }
                  console.log(reason);
                })
                .finally(() => handleCloseUnban());
            }}
          >
            Unban
          </Button>
          <Button variant="danger" onClick={handleCloseUnban}>
            Cancel
          </Button>
        </Modal.Footer>
      </Modal>

      <Modal show={showEdit} onHide={handleCloseEdit}>
        <Modal.Header closeButton>
          <Modal.Title>Ban details</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <form
            id="edit-form"
            onSubmit={(event) => {
              event.preventDefault();
            }}
          >
            <table style={{ width: "100%", textAlign: "center" }}>
              <tbody>
                <tr>
                  <td style={tdStyleDescription}>Player Name</td>
                  <td style={tdStyleField}>
                    <TextField
                      label=""
                      variant="outlined"
                      size="small"
                      defaultValue={row.name}
                      style={fieldStyle}
                      onChange={(event) => {
                        let newEditDetailsData = editDetailsData;
                        newEditDetailsData["name"] = event.target.value;
                        setEditDetailsData(newEditDetailsData);
                      }}
                    />
                  </td>
                </tr>
                <tr>
                  <td style={tdStyleDescription}>Steam ID</td>
                  <td style={tdStyleField}>
                    <TextField
                      label=""
                      variant="outlined"
                      size="small"
                      style={fieldStyle}
                      defaultValue={row.authid}
                      onChange={(event) => {
                        let newEditDetailsData = editDetailsData;
                        newEditDetailsData["authid"] = event.target.value;
                        setEditDetailsData(newEditDetailsData);
                      }}
                    />
                  </td>
                </tr>
                <tr>
                  <td style={tdStyleDescription}>Reason</td>
                  <td style={tdStyleField}>
                    <Select
                      native
                      labelId="reason-label"
                      id="reason"
                      style={fieldStyle}
                      onChange={(event) => {
                        let newEditDetailsData = editDetailsData;
                        newEditDetailsData["reason"] = event.target.value;
                        setEditDetailsData(newEditDetailsData);
                        setCustomReason(
                          newEditDetailsData["reason"] === "other"
                        );
                      }}
                    >
                      <option value="" selected="">
                        {" "}
                        -- Select Reason --{" "}
                      </option>
                      <optgroup label="Hacking">
                        <option value="Aimbot">Aimbot</option>
                        <option value="Antirecoil">Antirecoil</option>
                        <option value="Wallhack">Wallhack</option>
                        <option value="Spinhack">Spinhack</option>
                        <option value="Multi-Hack">Multi-Hack</option>
                        <option value="No Smoke">No Smoke</option>
                        <option value="No Flash">No Flash</option>
                      </optgroup>
                      <optgroup label="Behavior">
                        <option value="Team Killing">Team Killing</option>
                        <option value="Team Flashing">Team Flashing</option>
                        <option value="Spamming Mic/Chat">
                          Spamming Mic/Chat
                        </option>
                        <option value="Inappropriate Spray">
                          Inappropriate Spray
                        </option>
                        <option value="Inappropriate Language">
                          Inappropriate Language
                        </option>
                        <option value="Inappropriate Name">
                          Inappropriate Name
                        </option>
                        <option value="Ignoring Admins">Ignoring Admins</option>
                        <option value="Team Stacking">Team Stacking</option>
                      </optgroup>
                      <option value="other">Other Reason</option>
                    </Select>
                    <br />
                    <TextField
                      label=""
                      variant="outlined"
                      multiline
                      rows={2}
                      rowsMax={5}
                      defaultValue=""
                      style={{
                        display: customReason ? "block" : "none",
                        ...fieldStyle,
                      }}
                      onChange={(event) => {
                        let newEditDetailsData = editDetailsData;
                        newEditDetailsData["reason"] = event.target.value;
                        setEditDetailsData(newEditDetailsData);
                      }}
                    />
                  </td>
                </tr>
                <tr>
                  <td style={tdStyleDescription}>Ban Length</td>
                  <td style={tdStyleField}>
                    <Select
                      native
                      labelId="banlength-label"
                      id="banlength"
                      style={fieldStyle}
                      defaultValue={
                        (Number(row.length) / 60) as unknown as string
                      }
                      onChange={(event) => {
                        let newEditDetailsData = editDetailsData;
                        dayjs.extend(customParseFormat);
                        let newEndDate: number;
                        let length: number = event.target.value as number;
                        if ((length as unknown as string) === "0") {
                          newEndDate = 0;
                        } else {
                          newEndDate = dayjs(row.date_start, "DD.MM.YYYY-HH:mm")
                            .add(length as unknown as string, "minute")
                            .unix();
                        }
                        newEditDetailsData["ends"] = newEndDate as number;
                        newEditDetailsData["length"] = (length * 60) as number;
                        setEditDetailsData(newEditDetailsData);
                      }}
                    >
                      <option value="0">Permanent</option>
                      <optgroup label="minutes">
                        <option value="1">1 minute</option>
                        <option value="5">5 minutes</option>
                        <option value="10">10 minutes</option>
                        <option value="15">15 minutes</option>
                        <option value="30">30 minutes</option>
                        <option value="45">45 minutes</option>
                      </optgroup>
                      <optgroup label="hours">
                        <option value="60">1 hour</option>
                        <option value="120">2 hours</option>
                        <option value="180">3 hours</option>
                        <option value="240">4 hours</option>
                        <option value="480">8 hours</option>
                        <option value="720">12 hours</option>
                      </optgroup>
                      <optgroup label="days">
                        <option value="1440">1 day</option>
                        <option value="2880">2 days</option>
                        <option value="4320">3 days</option>
                        <option value="5760">4 days</option>
                        <option value="7200">5 days</option>
                        <option value="8640">6 days</option>
                      </optgroup>
                      <optgroup label="weeks">
                        <option value="10080">1 week</option>
                        <option value="20160">2 weeks</option>
                        <option value="30240">3 weeks</option>
                      </optgroup>
                      <optgroup label="months">
                        <option value="43200">1 month</option>
                        <option value="86400">2 months</option>
                        <option value="129600">3 months</option>
                        <option value="259200">6 months</option>
                        <option value="518400">12 months</option>
                      </optgroup>
                    </Select>
                  </td>
                </tr>
              </tbody>
            </table>
          </form>
        </Modal.Body>
        <Modal.Footer>
          <Button
            style={{ margin: "0.25rem" }}
            variant="success"
            type="submit"
            name="submit"
            form="edit-form"
            onClick={() => {
              axios
                .put(
                  `/api/bans/${row.bid}/`,
                  { ...editDetailsData, update_type: 2 },
                  {
                    headers: {
                      "Content-Type": "application/json",
                    },
                  }
                )
                .then((response: AxiosResponse) => {
                  setAlertMessage({
                    message: `${row.name}'s ban was edited`,
                    severity: "success",
                  });
                  getBans();
                })
                .catch((reason: AxiosError) => {
                  if (reason.response!.status === 403) {
                    setAlertMessage({
                      message: `Permission denied`,
                      severity: "error",
                    });
                  } else {
                    setAlertMessage({
                      message: `An error has occured`,
                      severity: "error",
                    });
                  }
                  console.log(reason);
                })
                .finally(() => {
                  handleCloseEdit();
                });
            }}
          >
            Save changes
          </Button>

          <Button
            style={{ margin: "0.25rem" }}
            variant="danger"
            onClick={handleCloseEdit}
          >
            Cancel
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
}

render(<App />, document.getElementById("app"));
