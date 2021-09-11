// todo.js
// Implementations for all the calls for the endpoints.
import Api from "../Api"

// Method to get a list of all
export const getTodoList = async () => {
    try {
      const response = await Api.get("/todos");
      return response;
    } catch (error) {
      console.error(error);
    }
};

// Get a details by name
export const getTodoById = async(id) => {
    try {
      const response = await Api.get(`/todo/${id}`);
      return response;
    } catch (error) {
      console.error(error);
    }
};
