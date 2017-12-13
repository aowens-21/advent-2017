import java.util.*;

public class CaptchaSolver
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);

        System.out.println("Please enter the captcha: ");
        String captcha = in.nextLine();

        System.out.println(computeSum(captcha.trim()));
    }

    //Adds digit if next character matches - Part One of Day 1
    private static int computeSum(String captcha)
    {
        int sum = 0;
        int captchaLength = captcha.length();

        for (int i = 0; i < captcha.length(); i++)
        {
            if (Character.getNumericValue(captcha.charAt(i)) == Character.getNumericValue(captcha.charAt((i+1) % captchaLength)))
            {
                sum += Character.getNumericValue(captcha.charAt(i));
            }
        }

        return sum;
    }

    //Adds digit if digit halfway around the circular list matches - Part Two of Day 1
    private static int computeSumHalfwayAcrossList(String captcha)
    {
        int sum = 0;
        int captchaLength = captcha.length();
        int halfCaptchaLength = captchaLength/2;

        for (int i = 0; i < captchaLength; i++)
        {
            if (Character.getNumericValue(captcha.charAt(i)) == Character.getNumericValue(captcha.charAt((i + halfCaptchaLength) % captchaLength)))
            {
                sum += Character.getNumericValue(captcha.charAt(i));
            }
        }

        return sum;
    }

}
