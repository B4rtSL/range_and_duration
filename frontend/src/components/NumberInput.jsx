import React from "react";

//Input box component

const NumberInput = ({ label, unit, value, setter }) => {
  const onChange = (e) => setter(() => parseFloat(e.target.value));
  return (
    <div className="form-control w-full max-w-xs">
      <label className="label">
        <span className="label-text">{label}</span>
        <span className="label-text-alt">Unit: {unit}</span>
      </label>
      <input
        type="number"
        placeholder="Type value here"
        className="input input-bordered w-full max-w-xs"
        value={value}
        onChange={onChange}
      />
    </div>
  );
};

export default NumberInput;
