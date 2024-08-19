import React from 'react';
import Button from '@mui/material/Button';

interface BtnType {
  type?: "button" | "submit" | "reset";
  disabled?: boolean;
  children: any,
  onClick?: () => void
}
export default function Btn(props: BtnType) {
  return <Button
    sx={{ width: 'fit-content' }}
    disabled={props.disabled}
    type={props.type || "button"}
    variant="contained"
    color="primary"
    onClick={props.onClick || (() => { })}
  >
    {props.children}
  </Button >
}