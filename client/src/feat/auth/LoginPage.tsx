import { LoadingSpinner } from "@/components/ui/LoadingSpinner";
import { useAuth } from "@/feat/auth/useAuth";
import { Navigate, useNavigate } from "react-router";
import { useForm } from "react-hook-form";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

export const LoginPage = () => {
  const { isAuthenticated, loading, login } = useAuth();
  const navigate = useNavigate();

  const form = useForm({
    defaultValues: {
      username: "",
      password: "",
    },
  });

  const onSubmit = async ({
    username,
    password,
  }: {
    username: string;
    password: string;
  }) => {
    const success = await login({ username, password });
    if (!success) {
      form.setError("root", { message: "Invalid username or password" });
    } else {
      navigate("/");
    }
  };

  if (loading) {
    return <LoadingSpinner />;
  }
  if (isAuthenticated) {
    return <Navigate to="/" />;
  }

  return (
    <div className="size-full flex items-center justify-center flex-col">
      <form
        onSubmit={form.handleSubmit(onSubmit)}
        className="flex flex-col gap-3 h-[300px]"
      >
        <div className="space-y-1">
          <h3 className="text-white">Username</h3>

          <Input
            id="username"
            {...form.register("username")}
            className="text-white"
          />
        </div>
        <div className="space-y-1">
          <h3 className="text-white">Password</h3>
          <Input
            id="password"
            {...form.register("password")}
            className={`text-white ${form.formState.errors.password && "bg-red"}`}
          />
        </div>
        <Button variant="secondary" className="mt-2" type="submit">
          Submit
        </Button>
        {form.formState.errors.root && (
          <p className="text-white">Invalid username or password</p>
        )}
      </form>
    </div>
  );
};
