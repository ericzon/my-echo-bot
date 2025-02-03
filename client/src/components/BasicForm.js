import React, { useState } from "react";
import {
  Button,
  Checkbox,
  Form,
  Input,
  InputNumber,
  Radio,
  Select,
} from "antd";
import Header from "./Header";

const formItemLayout = {
  labelCol: {
    xs: {
      span: 24,
    },
    sm: {
      span: 6,
    },
  },
  wrapperCol: {
    xs: {
      span: 24,
    },
    sm: {
      span: 14,
    },
  },
};

const plainOptions = ["A", "B"];
const defaultCheckedList = ["A"];
const selectOptions = [
  {
    value: "option1",
    label: "Option 1",
  },
  {
    value: "option2",
    label: "Option 2",
  },
  {
    value: "option3",
    label: "Option 3",
  },
];

const BasicForm = () => {
  const [checkedList, setCheckedList] = useState(defaultCheckedList);

  const onCheckBoxChange = (list) => {
    setCheckedList(list);
  };

  const onSelectChange = (value) => {
    console.log(`selected ${value}`);
  };

  const [form] = Form.useForm();
  return (
    <>
      <Header />
      <Form
        {...formItemLayout}
        form={form}
        style={{
          maxWidth: 600,
          marginTop: 50,
        }}
      >
        <Form.Item
          label="Input"
          name="Input"
          rules={[
            {
              required: true,
              message: "Please input!",
            },
          ]}
        >
          <Input />
        </Form.Item>

        <Form.Item
          label="InputNumber"
          name="InputNumber"
          rules={[
            {
              required: true,
              message: "Please input!",
            },
          ]}
        >
          <InputNumber
            style={{
              width: "100%",
            }}
          />
        </Form.Item>

        <Form.Item
          label="Select"
          name="Select"
          rules={[
            {
              required: true,
              message: "Please input!",
            },
          ]}
        >
          <Select
            options={selectOptions}
            onChange={onSelectChange}
            placeholder="Select an option"
          />
        </Form.Item>

        <Form.Item
          name="checkbox-group"
          label="Checkbox"
          rules={[
            {
              required: true,
              message: "Please input!",
            },
          ]}
        >
          <Checkbox.Group
            options={plainOptions}
            value={checkedList}
            onChange={onCheckBoxChange}
          />
        </Form.Item>

        <Form.Item
          name="radio-button"
          label="Radio Button"
          rules={[
            {
              required: true,
              message: "Please pick an item!",
            },
          ]}
        >
          <Radio.Group>
            <Radio.Button value="a">item 1</Radio.Button>
            <Radio.Button value="b">item 2</Radio.Button>
            <Radio.Button value="c">item 3</Radio.Button>
          </Radio.Group>
        </Form.Item>

        <Form.Item
          wrapperCol={{
            offset: 6,
            span: 16,
          }}
        >
          <Button type="primary" htmlType="submit">
            Submit
          </Button>
        </Form.Item>
      </Form>
    </>
  );
};
export default BasicForm;
