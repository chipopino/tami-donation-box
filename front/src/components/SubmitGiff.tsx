import React from 'react';
import Btn from 'components/Btn';
import { d_fileUpload } from 'methodes/routs';

export default function SubmitGiff() {
  return < form
    className='flex flex-col items-center justify-center w-fit'
    action={d_fileUpload()}
    method="post"
    encType="multipart/form-data"
  >
    <label className='w-fit'>upload 32x7 giff</label>
    <div className='flex flex-wrap items-center justify-center gap-2'>
      <input type="file" name="file" />
      <Btn type="submit">Submit</Btn>
    </div>

  </form >
}